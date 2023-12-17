import xlsxwriter

def write_product_data_to_excel(amazon_data, flip_data, file_name):
    # Workbook and Worksheet
    workbook = xlsxwriter.Workbook(file_name)
    worksheet = workbook.add_worksheet()

    # Headers
    headers = ["Product", "Price", "Rating"]
    for col_num, header in enumerate(headers):
        worksheet.write(0, col_num, header)
    print(amazon_data)

    # Track min/max vals
    min_amazon_price = float("inf")
    max_amazon_rating = -float("inf")
    min_flip_price = float("inf")
    max_flip_rating = -float("inf")

    # Amazon Data
    for row_num, item in enumerate(amazon_data, start=1):
        # Track min/max
        price = float(item[1])
        rating = float(item[2].split()[0])

        if price < min_amazon_price:
            min_amazon_price = price
        if rating > max_amazon_rating:
            max_amazon_rating = rating

        # Write row
        for col_num in range(len(headers)):
            cell_format = None
            if (col_num == 1 and price == min_amazon_price) or (
                col_num == 2 and rating == max_amazon_rating
            ):
                cell_format = workbook.add_format({"bg_color": "yellow"})
            worksheet.write(row_num, col_num, item[col_num], cell_format)

    # Add space between
    worksheet.set_row(len(amazon_data) + 1, None, None, {"hidden": True})
    worksheet.set_row(len(amazon_data) + 2, None, None, {"hidden": True})

    # Amazon Header
    worksheet.merge_range(
        len(amazon_data) + 3,
        0,
        len(amazon_data) + 3,
        2,
        "Amazon",
        workbook.add_format({"bold": True}),
    )

    # flip Data
    for row_num, item in enumerate(flip_data, start=len(amazon_data) + 4):
        # Track min/max
        price = float(''.join(str(item) for item in item[1].split(',')))
        rating = float(item[2].split()[0])

        if price < min_flip_price:
            min_flip_price = price
        if rating > max_flip_rating:
            max_flip_rating = rating

        # Write row
        for col_num in range(len(headers)):
            cell_format = None
            if (col_num == 1 and price == min_flip_price) or (
                col_num == 2 and rating == max_flip_rating
            ):
                cell_format = workbook.add_format({"bg_color": "yellow"})
            worksheet.write(row_num, col_num, item[col_num], cell_format)

    # flip Header
    worksheet.merge_range(
        len(amazon_data) + len(flip_data) + 5,
        0,
        len(amazon_data) + len(flip_data) + 5,
        2,
        "flip",
        workbook.add_format({"bold": True}),
    )

    workbook.close()
    print("Excel file written successfully!")

# if __name__ == '__main__':
#     amazon_data = [["Wireless Mouse A", "599", "4.3 stars",None], ["Wireless Mouse B", "595", "3.6 stars",None]]
#     flip_data = [["Wireless Mouse X", "590", "4.5 stars",None], ["Wireless Mouse Y", "595", "4.2 stars",None]]
#     write_product_data_to_excel(amazon_data, flip_data, "output_file.xlsx")
