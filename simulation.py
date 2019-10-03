import cv2
import numpy as np
import random
import showLogData
import timePredict
import os

class simulation():
	print("simulation")

	def __init__(self, path, i_path, temprature, wind_speed, wind_nature, co2_level, hclo3_level, base_level, co_level, AH_level, RH_level, soil_moisture, PH_level, light_intensity, UV_condition, IR_condition):
		print(path)
		green_area = simulation.detectGreen(path)
		print(green_area)

		infection_pattern = simulation.detectInfectionType(i_path, temprature, wind_speed, wind_nature, co2_level, hclo3_level, base_level, co_level, AH_level, RH_level, soil_moisture, PH_level, light_intensity, UV_condition, IR_condition)
		print(infection_pattern)

		simulation.runConvolution(path, green_area, infection_pattern)
		simulation.showVideoCreated()


	def detectGreen(image_path):
		# this will return the diteected green area of the input image
		print("image_path : ",image_path)
		img = cv2.imread(image_path)
		hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

		mask = cv2.inRange(hsv, (25, 150, 160), (86, 255,255))
		imask = mask>0
		green = np.zeros_like(img, np.uint8)

		green[imask] = img[imask]

		cv2.imshow("green.png", green)
		v = np.median(img)

		cv2.waitKey(0)

		k = cv2.waitKey(5) & 0xFF
		if k == 27:
		    cv2.destroyAllWindows()

		return green

	def detectInfectionType(infect_path, temprature, wind_speed, wind_nature, co2_level, hclo3_level, base_level, co_level, AH_level, RH_level, soil_moisture, PH_level, light_intensity, UV_condition, IR_condition):	
		print("detectInfectionType")
		i_img = cv2.imread(infect_path)
		img_size = np.shape(i_img)
		r_total = 0
		g_total = 0
		b_total = 0
		for i in range(img_size[0]):
			for j in range(img_size[1]):
				b_total += int(i_img[i][j][0])
				g_total += int(i_img[i][j][1])
				r_total += int(i_img[i][j][2])

		# getting the r_mean
		b_mean = b_total/(img_size[0]*img_size[1])
		showLogData.printLogData("MEAN BLUE COLOR VALUE : "+str(b_mean))
		g_mean = g_total/(img_size[0]*img_size[1])
		showLogData.printLogData("MEAN GREEN COLOR VALUE : "+str(g_mean))
		r_mean = r_total/(img_size[0]*img_size[1])
		showLogData.printLogData("MEAN RED COLOR VALUE : "+str(r_mean))
		cv2.waitKey(0)

		apply_img = [b_mean, g_mean, r_mean]
		timePredict.timePredict(temprature, wind_speed, wind_nature, co2_level, hclo3_level, base_level, co_level, AH_level, RH_level, soil_moisture, PH_level, light_intensity, UV_condition, IR_condition, apply_img)
		# print("#################### Special spot : ",img_size,", ",spredder)

		for ii in range(img_size[0]):
			for jj in range(img_size[1]):
				i_img[ii][jj][0] = apply_img[0]
				i_img[ii][jj][1] = apply_img[1]
				i_img[ii][jj][2] = apply_img[2]

		# cv2.imshow("INFECTION IMAGE", i_img)

		k = cv2.waitKey(5) & 0xFF
		if k == 27:
		    cv2.destroyAllWindows()

		return i_img


	def runConvolution(original_img_path, green_area, infection_p):
		# print("######################   new_dots : ",timePredict.new_dots)
		print("runConvolution")
		print(original_img_path)
		print(green_area)
		print(infection_p)

		original_img = cv2.imread(original_img_path)
		img_size = np.shape(original_img)


		# img_size and dot_density will be exported
		# tp = timePredict.timePredict
		# img_size, spredder = tp.__init__(temprature, wind_speed, wind_nature, co2_level, hclo3_level, base_level, co_level, AH_level, RH_level, soil_moisture, PH_level, light_intensity, UV_condition, IR_condition, img_size)
		# img_size, spredder = timePredict.timePredict(temprature, wind_speed, wind_nature, co2_level, hclo3_level, base_level, co_level, AH_level, RH_level, soil_moisture, PH_level, light_intensity, UV_condition, IR_condition, infection_p)

		# print(img_size,", ",spredder)
		count_row = 0
		count_pxcel = 0

		columns = int(img_size[0]/40)
		rows = int(img_size[1]/40)
		print("columns :",columns," rows : ",rows)

		dots = 0
		film_frams = [None] * 50
		for frames in range(50):
			dots = (frames+1) * 1000
			# print(dots)
			print((dots/50000)*100,"% PERCENT COMPLETED...")
			for x in range(dots):
				# print((dots/50000)*100,"% PERCENT COMPLETED...")
				i = random.randint(0,img_size[0]-1 )
				j = random.randint(0,img_size[1]-1)
		
				temp_o_list = original_img[i][j]
				temp_g_list = green_area[i][j]
		
				if((temp_o_list[0] == temp_g_list[0]) & (temp_o_list[1] == temp_g_list[1]) & (temp_o_list[2] == temp_g_list[2])):
					temp_o_list[0] = infection_p[0][0][0]
					temp_o_list[1] = infection_p[0][0][1]
					temp_o_list[2] = infection_p[0][0][2]
						#  & int(j/20)%2 == 0
				count_pxcel += 1
			film_frams[frames] = original_img
			day_lable = "("+str(frames+1)+") "+str((frames+1)%10+1)+" Of Day "+str(int((frames+1)/10)+1)
			# cv2.imwrite("E:\\ZZZZZ\\FIT\\pics\\"+day_lable+".jpg", original_img)
			
			dirName = 'final_result'

			if not os.path.exists(dirName):
				os.mkdir(dirName)
				print("Directory " , dirName ,  " Created ")

			cv2.imwrite("final_result\\"+day_lable+".jpg", original_img)

		cv2.waitKey(0)

	def showVideoCreated():
		print("showVideoCreated")


# frame = cv2.
# app = simulation("E:\\ImageProcessing\\17.02.2019\\bee.jpg", "E:\\ZZZZZ\\FIT\\infec.jpg")
# app = simulation("E:\\ImageProcessing\\17.02.2019\\bee.jpg", "E:\\ZZZZZ\\FIT\\apple.jpg")
# app = simulation("E:\\ZZZZZ\\FIT\\1.jpg","E:\\ZZZZZ\\FIT\\infec.jpg")
