# Build and Run 
```
docker build -t pconv:ver1 .
docker run -it --gpus all -v /home/no_anaconda/Desktop/docker_Pconv/dataset:/src_data pconv:ver1 /bin/bash

python3 main.py --train /src_data --test  /src_data --val /src_data
```
