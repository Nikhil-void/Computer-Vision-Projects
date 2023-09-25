from xml.dom import minidom
import numpy as np
import cv2
import pandas as pd

def draw_circ(img, point, color=(0,255,0), thick=1):
    img = cv2.circle(img, point, thick, color, thick)
    return img

def show_img(img):
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    
def write_image(title,img):
    cv2.imwrite("%s.jpeg" % title, img)

def get_projection_matrixes():
    final_data = []
    for i in range(8):
        data = minidom.parse('input_data\\calibration\\cam0%s.xml' % i).getElementsByTagName('camera').pop(0).childNodes[0].data.strip().split(' ')
        data = [float(j) for j in data if j != '']
        data = np.array(data).reshape(3,4)
        final_data.append(data)
    return final_data



def generate_voxel_grid(total_points):
    x = np.linspace(-2.5,2.5,total_points)
    y = np.linspace(-3.0,3.0,total_points)
    z = np.linspace(0,2.5,total_points)
    grid = np.array(np.meshgrid(x,y,z)).T.reshape(-1,3)
    grid = np.pad(grid, ((0,0),(0,1)), mode='constant', constant_values=1)
    grid = np.pad(grid, ((0,0),(0,1)), mode='constant', constant_values=0)
    return grid 


def print_voxel_grids():
    mat = get_projection_matrixes()
    grid = generate_voxel_grid()
    for i in range(8):
        proj_mat = mat[i]
        img = cv2.imread("input_data//silh_cam0%s_00023_0000008550.pbm" % i)
        n_img = img.copy()
        index = []
        result = proj_mat@grid[:,0:4].T
        result = result.T
        final_result = np.zeros([result.shape[0], 2])
        final_result[:, 0] = result[:,0] / result[:,2]
        final_result[:, 1] = result[:,1] / result[:,2]
        for val in final_result.astype("int"):
            n_img = draw_circ(n_img, val)
        write_image("voxel_grid_%s" % i, n_img)

def get_image_coordinate(proj_mat, point_3d):
    result = proj_mat@point_3d.T
    result = result.T
    final_result = np.zeros([result.shape[0], 2])
    final_result[:, 0] = result[:,0] / result[:,2]
    final_result[:, 1] = result[:,1] / result[:,2]
    final_result = final_result.astype("int")
    return final_result
        
def get_visual_hull(total_points):
    concat_voxel = []
    grid = generate_voxel_grid(total_points)
    print("Empty Grid Generated")
    for i in range(8):
        img = cv2.imread("input_data//silh_cam0%s_00023_0000008550.pbm" % i)
        proj_mat = get_projection_matrixes()[i]

        final_result = get_image_coordinate(proj_mat, grid[:,0:4])


        final_result[:,1][final_result[:,1] >= img.shape[0]] = img.shape[0]-1
        final_result[:,0][final_result[:,0] >= img.shape[1]] = img.shape[1]-1
        final_result[:,1][final_result[:,1] < 0 ] = 0
        final_result[:,0][final_result[:,0] < 0 ] = 0

        voxel_pixels = img[final_result[:,1], final_result[:,0]]
        if type(concat_voxel)== list :
            concat_voxel = voxel_pixels.copy()
        else:
            concat_voxel = np.concatenate((concat_voxel, voxel_pixels), axis=1)
        print("Voxel grid generated for Image %s" % i)
    grid[:,4] = np.all(concat_voxel, axis=1)
    print("Occupied and Empty distinguished Voxel grid generated")
    return grid

def calc_surface_voxel(grid, total_points):
    surface_voxel = []
    nd_grid = grid.reshape(total_points,total_points,total_points,5)
    print("Calculating Surface Voxel from Voxel grid")
    for x in range(1, total_points):
        for y in range(1, total_points):
            for z in range(1, total_points):
                if nd_grid[x,y,z,4] == 1:
                    blob = nd_grid[x-1:x+2, y-1:y+2, z-1:z+2]
                    if not np.sum(blob[:,:,:,4]) == 27:
                        #nd_grid[x,y,z,4] = 2
                        value = nd_grid[x,y,z].tolist()
                        value.extend([x,y,z])
                        surface_voxel.append(value)
    print("Surface Voxel calculated")
    return np.array(surface_voxel), nd_grid

def write_ply_file(data, all_color, textured, file_name):
    data = np.round(data, 5)
    data = np.char.mod('%f', data)
    
    header = """ply
format ascii 1.0
element vertex %s
property float x
property float y
property float z
property uchar red
property uchar green 
property uchar blue
element face 0
end_header\n""" % (data.shape[0])
    
    body = ""
    for indx, i in enumerate(data[:,:3]):
        if textured:
            color = all_color[indx]
            color = [str(int(c)) for c in color]
        else:
            color = ['0','0','0']
        body += " ".join(i)
        body += " "
        body += " ".join(color)
        body += "\n"
    
    final_ply = header + body
    
    with open("Output_data\\%s.ply" % file_name, "w") as file1:
        file1.write(final_ply)
        
def visualize_3d_model(file):
    import open3d as op3
    cloud = op3.io.read_point_cloud("Output_data\\%s.ply" % file) # Read the point cloud
    op3.visualization.draw_geometries([cloud]) # Visualize the point cloud 

def normalize(vector):
    return vector / np.linalg.norm(vector)

def get_cam_center(p):
    from scipy.linalg import null_space
    cam = null_space(p)
    cam[0], cam[1], cam[2] = cam[0]//cam[3], cam[1]//cam[3], cam[2]//cam[3]
    cam = np.delete(cam, 3)
    return cam

def sphere_intersect(center, radius, ray_origin, ray_direction):
    # This function referenced from following article https://medium.com/swlh/ray-tracing-from-scratch-in-python-41670e6a96f9
    b = 2 * np.dot(ray_direction, ray_origin - center)
    c = np.linalg.norm(ray_origin - center) ** 2 - radius ** 2
    delta = b ** 2 - 4 * c
    if delta > 0:
        t1 = (-b + np.sqrt(delta)) / 2
        t2 = (-b - np.sqrt(delta)) / 2
        if t1 > 0 and t2 > 0:
            return True
    return False

    

def get_data_and_color(point, surface_voxel):        
    intersected_points = []
    color = []
    for indx, p in enumerate(get_projection_matrixes()):
        current_intersected = []
        cam = get_cam_center(p)
        d = normalize(cam-point)

        for cur_ind, cur_point in enumerate(surface_voxel):
            cur_point = cur_point[:3]
            if cur_point.tolist() == point.tolist():
                continue
            stepped_point = point + d*0.01
            intersect = sphere_intersect(cur_point, 0.008, stepped_point, d)
            if intersect:
                current_intersected.append(cur_point.tolist())
        
        if len(current_intersected) == 0:
            point_2d = get_image_coordinate(p, np.append(point, 1).reshape(1,4))          
            img = cv2.imread("input_data//actual_images//cam0%s_00023_0000008550.png" % indx)
            color.append(img[point_2d[0][1], point_2d[0][0]])
    
    if len(color) == 0:
        color = [[250, 250, 250]]
        
    df = pd.DataFrame(np.array(color), columns=['b', 'g', 'r'])
    color = [df['r'].median(), df['g'].median(), df['b'].median()]
    data = point.tolist()
    string = " ".join([str(x) for x in data])
    string += ' '
    string += " ".join([str(int(x)) for x in color])
    string += '\n'

    return [data, color]