print("Sorting priority based on 1st character of item (highest to lowest):\n"
      "1) Special characters(Empty Space, Comma, Exclamination mark, etc.) \n"
      "2) Numbers \n"
      "3) Upper case characters \n"
      "4) Lower case characters \n")
l = input("Seperate each item of list with a comma(,)\n"
          "Enter Item/s: ").split(sep=',')
sortedl = sorted(l)
print(f"Original list: {l}\n"
      f"Sorted list: {sortedl}")
