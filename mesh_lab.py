import meshlabxml as mlx
import os

def create_mesh(Meshlab_adr,input_adr,output_adr,filter_adr):
    meshlabserver_path = Meshlab_adr
    os.environ['PATH'] = meshlabserver_path + os.pathsep + os.environ['PATH']
    mlx.run(file_in=input_adr, file_out=output_adr, output_mask='-m fc vc vn sa', script=filter_adr)
    return
