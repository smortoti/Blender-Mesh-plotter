
import csv
from mesh_lab import create_mesh

def csv_to_ply(address):
    with open(address, 'r') as csv_data_count:
        csv_read_count = csv.reader(csv_data_count , delimiter= ',')
        no_vertices = 0
        for _ in csv_read_count:
            no_vertices += 1
        vertices = "element vertex " + str(no_vertices)

    with open(address, 'r') as csv_data:
        csv_read = csv.reader(csv_data, delimiter=',')
        header_info = ["ply",
                "format ascii 1.0",
                "comment made by seyram",
                vertices,
                "property float x",
                "property float y",
                "property float z",
                "property float nx",
                "property float ny",
                "property float nz",
                "property uchar red",
                "property uchar green",
                "property uchar blue",
                "property uchar alpha",
                "element face 0",
                "property list uchar int vertex_indices",
                "end_header"]

        #CLEAR FILE
        clear = open("C:\\Users\\smort\\Desktop\\Desktop\\MESHPLOT\\pointcloud_files\\pointcloud.ply",'w')
        clear.write("")
        clear.close()
        ######################################
        ply_data = open("C:\\Users\\smort\\Desktop\\Desktop\\MESHPLOT\\pointcloud_files\\pointcloud.ply",'a')
        for head in header_info:
            ply_data.write(head)
            ply_data.write('\n')

        for row in csv_read:
            row_no = len(row)
            for i in range(0, row_no):
                if (i == 3):
                    #DEFAULT NORMAL COORDINATES
                    ply_data.write("0 ")
                    ply_data.write("0 ")
                    ply_data.write("0 ")

                    ply_data.write(str(row[i]))
                    ply_data.write(" ")

                else:
                    ply_data.write(str(row[i]))
                    ply_data.write(" ")
            ply_data.write('\n')

        print("out")
        ply_data.close()
    return




csv_to_ply("C:\\Users\\smort\\Desktop\\Desktop\\MESHPLOT\\csv_input\\coordinate2.csv")
#import_pointcloud("C:\\Users\\smort\\Desktop\\Desktop\\MESHPLOT\\pointcloud_files\\pointcloud.ply")
create_mesh('C:\\Program Files\\VCG\\MeshLab','C:/Users/smort/Desktop/Desktop/MESHPLOT/pointcloud_files/pointcloud.ply','C:/Users/smort/Desktop/Desktop/MESHPLOT/mesh_files/mesh.ply','C:/Users/smort/Desktop/Desktop/MESHPLOT/meshlab_filter_script/800_n_ballpoint.mlx')





