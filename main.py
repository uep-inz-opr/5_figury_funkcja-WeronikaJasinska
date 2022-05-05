from math import sqrt

def figures():
  fig_num = input()
  pi = 3.14
  measurements_array = []
  for index in range(int(fig_num)):
    fig_properties = input().split(" ")
    fig_properties_arr = [float(x) for x in fig_properties]
    if len(fig_properties_arr) == 1:
      circle = pi*((fig_properties_arr[0])**2)
      measurements_array.append(circle)
    if len(fig_properties_arr) == 2:
      rectangle = fig_properties_arr[0]*fig_properties_arr[1]
      measurements_array.append(rectangle)
    if len(fig_properties_arr) ==3:
      formula1 = (fig_properties_arr[0]+ fig_properties_arr[1]+ fig_properties_arr[2])/2
      triangle = sqrt(formula1*(formula1-fig_properties_arr[0])*(formula1-fig_properties_arr[1])*(formula1-fig_properties_arr[2]))
      measurements_array.append(triangle)
    if len(fig_properties_arr)>=4:
      print("Błąd: można podać maksymalnie 3 liczby")
      return None



  measurements_array_float = [float(x) for x in measurements_array]
  total = round((sum(measurements_array_float)),2)

  print(total)


figures()
