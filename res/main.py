# import PyPDF2
# import json
# from typing import List
#
#
# def search_word_in_pdfs(pdf_files: List[str], target_word: str) -> list:
#     """
#     在多个PDF文件中搜索目标词语的所有位置，仅返回x.y格式的页码列表（JSON格式）
#     页码格式：x.y（x=第几个PDF文件，y=该PDF内的页码）
#
#     参数:
#         pdf_files: PDF文件路径列表（如["A1.pdf", "A2.pdf", "B1.pdf"]）
#         target_word: 要查询的目标词语
#
#     返回:
#         JSON格式的字符串，结构为：["1.5", "2.3", "3.8", ...]
#     """
#     # 仅保留x.y格式的页码列表
#     pages_list = []
#
#     # 遍历每个PDF文件（x从1开始，代表第x本书）
#     for file_index, pdf_file in enumerate(pdf_files, start=1):
#         try:
#             with open(pdf_file, 'rb') as file:
#                 pdf_reader = PyPDF2.PdfReader(file)
#
#                 # 遍历当前PDF的每一页（y为页码）
#                 for page_num, page in enumerate(pdf_reader.pages, start=1):
#                     try:
#                         page_text = page.extract_text()
#                         if not page_text:
#                             continue
#
#                         # 检查当前页是否包含目标词语（只要有匹配就记录页码）
#                         if target_word in page_text:
#                             # 构造x.y格式的页码并加入列表
#                             page_format = f"{file_index}.{page_num - 5}"
#                             # 去重：避免同一页码多次添加（如果一页内有多个匹配）
#                             if page_format not in pages_list:
#                                 pages_list.append(page_format)
#
#                     except Exception:
#                         continue  # 跳过页码读取失败的情况
#
#         except Exception:
#             continue  # 跳过文件处理失败的情况
#
#     # 转换为JSON字符串返回（纯页码列表）
#     return pages_list  # json.dumps(pages_list, ensure_ascii=False, indent=4)
#
#
# # ------------------- 调用示例 -------------------
# if __name__ == "__main__":
#     # 配置参数
#     pdf_files = ["A1.pdf", "A2.pdf", "B1.pdf"]  # 第1本:A1.pdf 第2本:A2.pdf 第3本:B1.pdf
#     config = {
#         "words": [],
#         "length": [[], [], []],  # 0->2
#         "difficulty": {
#             "easy": [],
#             "normal": [],
#             "hard": []
#         },
#         "describe": []
#     }
#     # target_word = "梁启超"  # 替换为要查询的词语
#     #
#     # # 调用函数获取仅含页码的JSON结果
#     # json_result = search_word_in_pdfs(pdf_files, target_word)
#     #
#     # # 打印结果
#     # print("仅保留页码的查询结果（x.y格式）：")
#     # print(json_result)
#     #
#     # # 可选：保存结果到文件
#     # with open("./test/only_pages_result.json", "w", encoding="utf-8") as f:
#     #     f.write(json_result)
#     dataInfo = {}
#     with open("data.json", "r", encoding="utf-8") as file:
#         data = json.load(file)
#     id = 0
#     for text in data:
#         if len(text) <= 1:
#             continue
#         print(f"{id + 1}: {text}")
#         tmp = search_word_in_pdfs(pdf_files, text)
#
#         if not tmp:
#             continue
#
#         info = {
#             "info": text,
#             "pages": tmp,
#             "describe": None
#         }
#         id += 1
#         # with open(f"res/DataBase/{id}", "w", encoding="utf-8") as f:
#         #     f.write(json.dumps(info, ensure_ascii=False, indent=2))
#         dataInfo[str(id)] = info
#
#         config["words"].append(id)
#         if 2 <= len(text) <= 4:
#             config["length"][len(text) - 2].append(id)
#         config["difficulty"]["normal"].append(id)
#
#     with open("DataBase/config", "w", encoding="utf-8") as file:
#         file.write(json.dumps(config, ensure_ascii=False, indent=2))
#     with open("DataBase/data", "w", encoding="utf-8") as file:
#         file.write(json.dumps(dataInfo, ensure_ascii=False, indent=2))
import json

with open("DataBase/config", "rw", encoding="utf-8") as f:
    info = json.loads(f.read())
    for i in range(len(info["words"])):
        info["words"][i] = str(info["words"][i])
    for i in range(len(info["length"])):
        for j in range(len(info["length"][i])):
            info["length"][i][j] = str(info["length"][i][j])
    for i in range(len(info["difficulty"]["easy"])):
        info["difficulty"]["easy"][i] = str(info["difficulty"]["easy"][i])
    for i in range(len(info["difficulty"]["normal"])):
        info["difficulty"]["normal"][i] = str(info["difficulty"]["normal"][i])
    for i in range(len(info["difficulty"]["hard"])):
        info["difficulty"]["hard"][i] = str(info["difficulty"]["hard"][i])
    print(json.dumps(info,indent=2))