import xlsxwriter

def write_product_data_to_excel(amazon_data, myntra_data, file_name):
    # Workbook and Worksheet
    workbook = xlsxwriter.Workbook(file_name)
    worksheet = workbook.add_worksheet()

    # Headers
    headers = ["Product", "Price", "Rating"]
    for col_num, header in enumerate(headers):
        worksheet.write(0, col_num, header)

    # Track min/max vals
    min_amazon_price = float("inf")
    max_amazon_rating = -float("inf")
    min_myntra_price = float("inf")
    max_myntra_rating = -float("inf")

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

    # Myntra Data
    for row_num, item in enumerate(myntra_data, start=len(amazon_data) + 4):
        # Track min/max
        price = float(item[1])
        rating = float(item[2].split()[0])

        if price < min_myntra_price:
            min_myntra_price = price
        if rating > max_myntra_rating:
            max_myntra_rating = rating

        # Write row
        for col_num in range(len(headers)):
            cell_format = None
            if (col_num == 1 and price == min_myntra_price) or (
                col_num == 2 and rating == max_myntra_rating
            ):
                cell_format = workbook.add_format({"bg_color": "yellow"})
            worksheet.write(row_num, col_num, item[col_num], cell_format)

    # Myntra Header
    worksheet.merge_range(
        len(amazon_data) + len(myntra_data) + 5,
        0,
        len(amazon_data) + len(myntra_data) + 5,
        2,
        "Myntra",
        workbook.add_format({"bold": True}),
    )

    workbook.close()
    print("Excel file written successfully!")

if __name__ == '__main__':
    amazon_data = [["Wireless Mouse A", "599", "4.3 stars"], ["Wireless Mouse B", "595", "3.6 stars"]]
    myntra_data = [["Wireless Mouse X", "590", "4.5 stars"], ["Wireless Mouse Y", "595", "4.2 stars"]]
    write_product_data_to_excel(amazon_data, myntra_data, "output_file.xlsx")
