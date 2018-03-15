
import win32com.client as cl

e_app = cl.gencache.EnsureDispatch("Excel.Application")
e_app.Visible = True
wb = e_app.Workbooks.Open("C:\\Users\\shashank.pochampalli\\Documents\\DAutomation.xlsx")
ws = wb.Worksheets("Sheet1")
ws.Cells(1,1).Value = "Btwin"

