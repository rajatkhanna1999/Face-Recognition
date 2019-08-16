# Face-Recognition
A Python code for recogntion of a person via face detection and recognition.
We trained model on outourtraining data and when a testing image comes or a frame is extracted from the live stream , our models matches the two images on basis of simlarity by considering 68 points on
the face . Modl used classifer which uses SVM(support vector machine) . Model uses dlib , face_recognition and opencv library in our model . In order to improve the accuracy , we tweeked several parameters like changing tolerance of our model etc .The model makes a square box on the faces of the people detected and if the person is known then it recoganises it and displays the name else it displays unknown.

## Features
* The system  detects and recognises faces of people in live stream.
* It has quite high accuracy and we achieved this by tuning with other
parameters such as tolerance etc.
* It is integrated well with hardware like raspberry pie.

## Features
* We may deploy the system at the entrance of the class/institute/hostel. Every
authorized member is required to get access through the system.We may also
choose an audio to announce an un-authorized access and alarm the security
centre.
* We may deploy this model for automated attendance system.


### Fork 

```sh
$ git clone https://github.com/rajatkhanna1999/Face-Recognition.git
```

#### Screenshots
<img src="https://user-images.githubusercontent.com/31288037/63163695-ce6b6f80-c043-11e9-8308-5e869eed265a.jpeg" width="340" height="567">
<img src="https://user-images.githubusercontent.com/31288037/63163777-0672b280-c044-11e9-81b3-d66ed8b95e2d.jpeg" width="340" height="567">






