# ct_tongji

此项目为与同济医学院合作的数据集搭建。

目前只有从dicom到raw的代码。后续持续更新。diconm到raw的代码依赖SIMPLEITK包，用命令行python.exe DicomSeriesReader.py <input_directory> <output_file>直接运行。

在test_data文件夹中有一例病例的完整CT数据，包含多个分辨率的CT图。可以使用RaidiAnt Dicom软件直接查看。

simpleITK需要使用Fiji作为外置图片查看器。
