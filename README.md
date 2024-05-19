# AI Sentinel | O D S
<div>
   <a href="https://github.com/iamvikramkumar/AI-SENTINEL/wiki">
<!--    <img src="https://github.com/iamvikramkumar/AI-Sentinel-Enhancing-Video-Surveillance-with-Intelligent-Monitoring/assets/89016145/4630c877-0c88-4006-bd73-02fbd67bf241" alt="person" width="600" height="400"> -->
      <img src="https://github.com/iamvikramkumar/AI-SENTINEL/assets/89016145/8531ba14-3336-4788-bad9-efba07ac5279" alt="person">
</div> 


**Welcome to the AI Sentinel Research Project! This initiative is dedicated to exploring and advancing the capabilities of video surveillance through the integration of artificial intelligence for intelligent monitoring.**

This is a project to perform fall detection, vehicle crash detection and social distancing detection from CCTV cameras in real-time.

## How YOLO works ?

![Alt text](https://cdn-images-1.medium.com/max/1024/1*bSLNlG7crv-p-m4LVYYk3Q.png)

YOLO stands for You Only Look Once. It is used for object detection
To perform object detection on an image it looks at an image only once in a very clever way unlike R-CNN which takes several instances of the same image to perform detection. 

YOLO divides an image into a grid and several bounding boxes are formed. Then a confidence score is taken for each boundary box to see whether an bounding box contains any object within it. The confidence score is high if the object inside the box matches the pre-trained YOLO dataset ( [COCO Dataset](https://cocodataset.org/) ). The higher the confidence score, the higher the probability that a bounding box contains an object. Now several bounding boxes will intersect with each other. More the bounding boxes intersect, more is the probability that there is an object inside that box. Now we only keep those bounding boxes whose confidence score is more than threshold value lets say 30%. Now we match these bounding boxes with already known features of an object like person, car and classify them.

The good thing about YOLO is that all the predictions in the boxes are made at the same time i.e. the neural networks just ran only once.
And that is why YOLO is powerful and fast.

## Sample Output 

![Screenshot (715)](https://github.com/iamvikramkumar/AI-SENTINEL/assets/89016145/dcf9f3d9-d2f8-41f8-99f4-061e5bc84ac6)
<br>
Vehicle Detection Output

![image](https://github.com/iamvikramkumar/AI-SENTINEL/assets/89016145/4ae21db0-c0b1-4e25-8c63-ea74a5189435)
<br>
Crash Detection Output

![Screenshot (737)](https://github.com/iamvikramkumar/AI-SENTINEL/assets/89016145/3983740a-f7ce-4646-a2bb-eecc3c7f0a87)
<br>
Fall Detection Output



## How to Contribute
**Your contribution to the AI Sentinel Research Project is valuable! Here's how you can get involved:**

**🤝 Collaboration: If you're passionate about AI, surveillance, or security, feel free to join the research efforts. Reach out to [ {soon updated} email.com ] to express your interest.**

**📚 Literature Review: If you have expertise in relevant literature, contribute by sharing insights, research papers, or studies related to video surveillance and AI.**

**🖥️ Technical Contributions: Developers are encouraged to contribute code, algorithms, or technical solutions to advance the project. Fork the repository, make your changes, and submit a pull request.**

## Future Plans
**🔜 Upcoming Milestones: We have exciting plans for the future, including the implementation of prototypes, testing, and collaboration with industry partners.**

**💬 Community Involvement: We aim to foster a vibrant community around AI Sentinel. Regular updates, discussions, and feedback are encouraged.**

## Contact
**For inquiries, collaboration, or more information, please contact us.**

**Thank you for your interest in the AI Sentinel Research Project! Together, let's shape the future of intelligent video surveillance.**
