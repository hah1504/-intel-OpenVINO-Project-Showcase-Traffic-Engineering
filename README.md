# Intel OpenVINO Project Showcase Traffic Engineering

This project is one of our attempt to solve the global Traffic Issues and also the road occupancy of vehicles.
Traffic Engineering For Measuring Traffic Count Using Python and OpenCV

## Abstract

The Project is about detecting the road occupancy from using Python and OpenCV The Traffic Control has been one of the most prominent global issues. Some of the problems were measuring traffic size and road occupancy. To solve this problem, the concept of smart traffic control system was introduced. Smart traffic control system, as the name suggests, is about applying the concepts of artificial intelligence (Edge based, Cloud based or hybrid) and using sensors and camera to improve the efficiency of the traffic control with little human intervention required. Our project focuses on delivering such a system by enabling dynamic control of the traffic signal based on the number of cars moving. 

![central idea](https://user-images.githubusercontent.com/55000923/76172472-a06e8980-6153-11ea-9624-eab6c662c2de.png)


## CORE CONCEPTS

This project is built around edge A.I, background subtraction algorithm for vehicle detection along with object detection, object tracking, and event classification technique. This system is also given the ability to make predictions on its own using the machine learning algorithms and the input data.

## FUNCTION

This project is built around the concept of calculating dimension of vehicle counting along with object detection, object tracking, and event classification technique.

### Vehicle Dimension Detection:

We use Python with OpenCV video stream for automatic vehicle detection and vehicle counting and connecting it to Intel OpenVino Toolkit in order to optimize the model. 
Mounted cameras will scan the area for all vehicle’s movement and it will take their dimensions in real time. The background of Images taken from video sequence are extracted. The extracted background is used in subsequent analysis to detect and classify moving vehicles as light vehicles, heavy vehicles and motorcycle. Then it will relay the information to the other adjacent sensors and help them predict the target’s next movement. Finally the information is then transferred to the nearest station for further processing.
The system is implemented using OpenCV image development kits and experimental results are demonstrated from real-time video taken from single camera.   This highway traffic counting process has been developed by background subtraction, image filtering, image binary and segmentation methods are used. This system is also capable of counting moving vehicles from pre-recorded videos.

## WORKING MECHANISM

The project is basically designed to work on edge device systems. which is connected on two areas, one is towards camera and second is towards sensors. From there it will take input and the output will be created in the form of images shown above. In the input it will be the vehicles' captured by the cameras. Anywhere on the road the car is presented it will move the lights towards that end.   Our model is deployed on edge applications (with cloud system used as backup in case of errors and connectivity issues) .
The project can also use popular cloud-based services like Google maps to give the passengers and custom cloud-based tracking apps to give police officers information regarding the state of a traffic route and the target vehicle using the data taken from the traffic camera in order to maintain smooth traffic flow and capture suspicious vehicles.

## Results

The following screenshots is the result of our project:
 
 
![cars123](https://user-images.githubusercontent.com/55000923/76172567-b597e800-6154-11ea-9e01-d576308754fa.jpg)  



![crpeedcars3](https://user-images.githubusercontent.com/55000923/76172576-c8aab800-6154-11ea-8032-31f14dfb1b08.png)  



![CARS_CROPPED3](https://user-images.githubusercontent.com/55000923/76172586-d6f8d400-6154-11ea-9ad2-ac70bfbcf1d5.png)  



![CARS_CROPPED](https://user-images.githubusercontent.com/55000923/76172590-dbbd8800-6154-11ea-95cf-597a98bc95d5.png)  



![cars2](https://user-images.githubusercontent.com/55000923/76172598-ea0ba400-6154-11ea-8b8e-9a3b48e88930.png)  



## Digital Image:
 
 
![cars with shadows](https://user-images.githubusercontent.com/55000923/76172687-a5ccd380-6155-11ea-8f9d-ed6760a5fcf0.png)  



![1_MAHBdrboF8YUM_krufvGlw](https://user-images.githubusercontent.com/55000923/76172690-aa918780-6155-11ea-8e84-9d4e76317934.png)  



![dilated](https://user-images.githubusercontent.com/55000923/76172698-bf6e1b00-6155-11ea-9d71-d5804823944b.png)  




![ERODE2](https://user-images.githubusercontent.com/55000923/76172794-897d6680-6156-11ea-851c-0af805d9114f.png)  




![ERODE4](https://user-images.githubusercontent.com/55000923/76172714-da408f80-6155-11ea-8a39-9b88d41fbf2d.png)  

 
 
 
### Prerequisites

Software: Windows or Linux operating system

Hardware includes

•	Intel 6th Generation and above Generation based processors
•	Minimum 8 GB RAM

### TOOLS

•	Google Map service  
•	Intel OpenVINO  
•	OpenCV  
•	Python  

## Conclusion:

The main objective of the project is to develop a traffic system where the traffic custodians can perform their tasks efficiently and assist in keeping the roads safe for the civilians. We have worked on the openVINO toolkit and put all our basic knowledge and the course content materials to use in order for us to implement Edge AI Model Deployment knowledge so we could deliver a good project.

### Members

•	Haseeb Ahmed Khan  
•	Syed Muhammad Masab Hashmi

Star this Repo, to encourages the team-members 😃

👍 This PROJECT looks great - It's ready for the SHOWCASE!  
