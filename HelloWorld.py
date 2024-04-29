from openpyxl import Workbook

def save_to_excel(data):
    # Create a new workbook
    wb = Workbook()
    # Select the active worksheet
    ws = wb.active

    # Write data to the first row of the worksheet
    ws.append(data)

    # Save the workbook
    wb.save("user_input.xlsx")
    print("Data saved to user_input.xlsx")

def main():
    # Get user input
    user_input = input("Enter data to save to Excel (separated by commas): ")
    # Split the input into a list of values
    data = user_input.split(',')
    # Save the data to Excel
    save_to_excel(data)

if __name__ == "__main__":
    main()
