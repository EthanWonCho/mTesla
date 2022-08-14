#include <opencv2/opencv.hpp>
#include <iostream>
using namespace std;
using namespace cv; 

int main()
{
      VideoCapture cap(0);           // Creating VideoCapture object and opening webcam
      if(!cap.isOpened())                  //Checking if opened  
      {
              cout << "Error opening Web cam" << endl;
               return -1;
      }
      while(1)
      {
               Mat frame;                                              // Creating Mat object
               cap >> frame;                                         // Capture frame-by-frame  
               if (frame.empty())                                // If the frame is empty, break immediately
                       break;
                imshow( "VdoFrame", frame );         // Display the frame 
                char a=(char)waitKey(25);                //Press ESC on keyboard to exit/
                if(a==27)
                      break;
         } 
         cap.release();                                         // When everything done, release the video capture object  
         destroyAllWindows();                           // Closes all the frames
         return 0;
}
