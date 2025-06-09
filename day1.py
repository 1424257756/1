import numpy as np


def sentinel_to_rgb(data):
    """
    将哨兵2号数据压缩并转换为RGB图像
    :param data: 输入数据 (5, H, W) 或 (H, W, 5)，数值范围0-10000
    :return: uint8类型的RGB图像 (H, W, 3)
    """
    # 确保数据是浮点类型
    data = data.astype(np.float32)

    # 统一数据形状为 (H, W, 5)
    if data.shape[0] == 5:
        data = np.moveaxis(data, 0, -1)  # 从 (5, H, W) -> (H, W, 5

    # 线性压缩到0-255范围
    data = (data / 10000.0) * 255.0
    data = np.clip(data, 0, 255).astype(np.uint8)

    # 提取RGB波段 (假设波段顺序: 0=蓝, 1=绿, 2=红)
    rgb = data[..., [2, 1, 0]]  # 顺序: 红(波段2), 绿(波段1), 蓝(波段0)

    return rgb


# 示例用法
if __name__ == "__main__":
    # 模拟输入数据 (5个波段, 512x512图像)
    # 实际使用时替换为真实数据
    h, w = 512, 512
    input_data = np.random.randint(0, 10001, size=(5, h, w))

    # 转换为RGB
    rgb_image = sentinel_to_rgb(input_data)

    # 检查结果 (H, W, 3) uint8数组
    print("RGB图像形状:", rgb_image.shape)
    print("像素值范围:", rgb_image.min(), "-", rgb_image.max())