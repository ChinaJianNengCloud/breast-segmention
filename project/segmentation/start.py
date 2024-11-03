import os
import subprocess


def main():


    # 设置 CUDA 路径

    # 你的其他代码
    CONFIG = "/mnt/f/yinda/qianyi/InternImage-master/InternImage-master/segmentation/configs/coco_stuff164k/mask2former_internimage_h_896_80k_cocostuff164k_ss.py"  # 你需要提供默认的配置文件路径
    GPUS = "1"
    PORT = os.environ.get('PORT', '29300')


    script_dir = os.path.dirname(os.path.abspath(__file__))
    python_path = os.path.join(script_dir, "..")
    os.environ['PYTHONPATH'] = f"{python_path}:{os.environ.get('PYTHONPATH', '')}"


    cmd = [
              "python", "-m", "torch.distributed.launch",
              "--nproc_per_node=" + GPUS,
              "--master_port=" + PORT,
              os.path.join(script_dir, "train.py"),
              CONFIG,
              "--launcher", "pytorch"
          ]

    subprocess.run(cmd)


if __name__ == "__main__":
    main()
