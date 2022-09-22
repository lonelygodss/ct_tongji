import SimpleITK as sitk


def read_dcm_series(dcm_path, logger=None):
    """
    此函数已考虑dcm中阶矩与斜率的tag
    输出的矩阵已按照世界坐标的顺序排列
    :param dcm_path:
    :param logger:
    :return: sitk格式图像; series_id
    """
    series_IDs = sitk.ImageSeriesReader.GetGDCMSeriesIDs(dcm_path)  # 获取该路径下的seriesid的数量
    nb_series = len(series_IDs)
    if nb_series > 1:
        if logger is not None:
            logger.info("nb_series > 1, series ids: %s" % series_IDs)
        else:
            print("nb_series > 1, series ids: %s" % series_IDs)
    series_file_names = sitk.ImageSeriesReader.GetGDCMSeriesFileNames(
        dcm_path
    )  # 获取该路径下所有的.dcm文件，并且根据世界坐标从小到大排序
    series_reader = sitk.ImageSeriesReader()
    series_reader.SetFileNames(series_file_names)

    image_sitk = series_reader.Execute()  # 生成3D图像
    return image_sitk, series_IDs[0]

