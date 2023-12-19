secs_str = input("Input seconds: ") # do not change this line
secs_int = int(secs_str)
hours = round(secs_int/3600)
minutes = round((secs_int % 3600) / 60)
seconds = round(((secs_int % 3600) % 60))
print("\n",hours,":",minutes,":",seconds) # do not change this line