# 原项目github网址
https://github.com/OpenGVLab/InternImage

# 项目介绍
该项目是用于分割人体模型的乳房(最终结果是用不同的颜色在原图中标注出来)，使用分割的sota模型(2023年10月份)进行迁移学习，是像素二分类的任务。

# 数据介绍
该数据是通过拍摄人体模型获得的数据，有4329张图片，每张图片中包含了一个模型至两个模型不等，
最原始的数据的mask文件是由json来标记的，我通过json数据转成了图片，与对应原图等长宽，乳房部分用白色标记，其余部分用黑色标记。
第一次实验将数据分成了train（4000）张，val(329)张。之后进行了数据增强，一共有2万张，包含downsize,downupsize,updownsize,upsize,意思分别是将图片resize成540x540，1024x512，512x1024，960x960。
目前数据集的根目录是slist \baidu\sjwlab\chenyinda\project\乳房分割模型\data
全体数据集:乳房分割实验数据集total
train数据集:train(4000)
val数据集:val(329)
dataup数据集(val不变):数据增强数据集

# 环境
需要在linux或者wsl中。按照原github安装即可。由于设备改动，本地无环境备份。

# 项目使用
项目的配置文件使用
总体配置文件 S:\baidu\sjwlab\chenyinda\project\乳房分割模型\project\segmentation\configs\coco_stuff164k\mask2former_internimage_h_896_80k_cocostuff164k_ss.py
S:\baidu\sjwlab\chenyinda\project\乳房分割模型\project\segmentation\configs\_base_\default_runtime.py
数据配置文件S:\baidu\sjwlab\chenyinda\project\乳房分割模型\project\segmentation\configs\_base_\datasets\coco-stuff164k.py
模型配置文件S:\baidu\sjwlab\chenyinda\project\乳房分割模型\project\segmentation\configs\_base_\models\mask2former_beit.py
运行规则配置规则S:\baidu\sjwlab\chenyinda\project\乳房分割模型\project\segmentation\configs\_base_\schedules\schedule_80k.py
预训练模型的目录S:\baidu\sjwlab\chenyinda\project\乳房分割模型\remodel
其中在总体配置文件中可以设置预训练模型的类别，分割的类别数，与训练的模型路径，数据resize的大小(GPU不足可以减小)，可以设置类别loss，CEloss，每个类别的权重，loss的权重
在数据配置文件中需要修改数据集的路径。
在模型配置文件中修改类别数，三个loss的权重，clsloss,diceloss,maskloss。

使用start.py即可运行训练脚本
在train.py的303行修改dongjie参数的值即可修改冻结的层数，冻结从1到5，1模型训练的参数最多，5模型训练的参数最少。

要想使用需要在安装的环境的mmseg包中datasets中添加S:\baidu\sjwlab\chenyinda\project\乳房分割模型\replace的两个文件，其中yinda.py定义了数据集类别数和使用的颜色，以及init.py定义初始化这个数据类。


# 项目结果
S:\baidu\sjwlab\chenyinda\project\乳房分割模型\result
包括tensorboard文件，txt记录，最终的模型参数。
如有必要，可以将该路径中的两个配置文件替换掉project中对应文件夹的文件。