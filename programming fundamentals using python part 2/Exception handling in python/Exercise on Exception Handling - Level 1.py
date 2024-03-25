def find_average(mark_list):
	total=0
	try:
		for i in range(0, len(mark_list)):
			total+=mark_list[i]
		marks_avg=total/len(mark_list)
		return marks_avg
	except IndexError:
		print("index error occured")
	except ZeroDivisionError:
		print("zero div error occured")
	except TypeError:
		print("Type error occured")
	except NameError:
		print("Name Error Occured")
	except:
		print("Some Error Occured")

try:
	m_list=[1,2,3,4]
	print("Average marks:", find_average(m_list))
except ValueError:
	print("Value error occured")
except:
	print("some error occured")