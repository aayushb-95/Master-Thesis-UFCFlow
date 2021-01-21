
## UFCFlow - Optical Flow Estimation Using Unsupervised Deep Learning

 - This repository contains the implementation of my Master Thesis titled: **UFCFlow - Optical Flow Estimation Using Unsupervised Deep Learning**.
 - Optical flow is the distribution of apparent velocities of movement of brightness patterns between two consecutive image frames.
 - The UFCFlow model is trained on the Flying Chairs and the MPI Sintel dataset.
 - Unsupervised learning approach is adopted for training the UFCFlow model.
 - For unsuprvised training four loss functions are used:
	 - **Photometric loss [7]**: Measures the photometric difference between the two image frames.
	 - **Structural Dissimilarity Index (SSIM) loss [6]**: Measures the structural dissimilarity value between the two image frames.
	 - **First-Order-Smoothness loss [7]**:  Measures the deviation from the smoothness assumption that neighboring pixels in an image frame move together
	 - **Second-Order-Smoothness loss [4]**: Higher-order smoothness loss for better regularization and encouraging collinearity. 
 - The UFCFlow model is inspired from the FlowNetC [1] model with modifications to the underlying architecture and adapted for the unsupervised traning methodology .
 
## UFCFlow Model Architecture
- **Overview diagram of the UFCFlow network for unsupervised optical flow estimation**
![enter image description here](https://github.com/aayushb-95/Master-Thesis-UFCFlow/blob/main/UFCFlow%20Architecture/UFCFlow.png)
 - **Contractive Network**
 ![enter image description here](https://github.com/aayushb-95/Master-Thesis-UFCFlow/blob/main/UFCFlow%20Architecture/UFCFlow-Contractive.png)
 - **Refinement Network**
![enter image description here](https://github.com/aayushb-95/Master-Thesis-UFCFlow/blob/main/UFCFlow%20Architecture/UFCFlow-Refinement.png)

## Results
![enter image description here](https://github.com/aayushb-95/Master-Thesis-UFCFlow/blob/main/UFCFlow%20Results/Result-Table.PNG)
 
## Datasets
- **Flying Chairs [1]**
  - The UFCFlow model is trained using 22,234 traning image pairs and tested using 638 testing image pairs.
  - The dataset can be downloaded from - https://lmb.informatik.uni-freiburg.de/data/FlyingChairs/FlyingChairs.zip
  - Extract the folder and use the images and .flo files from the flow folder.

- **MPI Sintel [2]**
  - The UFCFlow model is trained using 90-10 train-test split from the Clean and Final render category.
  - The MPI Sintel dataset is also used as a test set for the UFCFlow model trained on the Flying Chairs dataset
  - The dataset can be downloaded from - http://sintel.is.tue.mpg.de/downloads (Download the MPI-Sintel-complete.zip).
  - Extract the folder and use the images from the final folder and .flo files from the flow folder.



## Code Execution

### Dataframe Creation
- The UFCFlow model uses tf.data API to pass the data to the model. 
- To map the data values to the tf.data API and map function is used.
- This map function takes the inpt images from the dataframe.
- To create dataframe for the Flying Chairs dataset use - **Dataframe_Creation_FlyingChairs.py** and enter the path for the images and flow file from the extracted folder before executing the code.
-  To create dataframe for the MPI Sintel dataset use - **Dataframe_Creation_MPISintel.py** and enter the path for the images and flow file from the extracted folder. Execute the code separately for the clean pass and the final pass respectively with the corresponding path.



### UFCFlow Model Execution on Google Colab environment
- Upload the dataset on Google Drive.
- Upload the dataframes on Google Drive
- Upload the jupyter notebooks: **UFCFlow_Sintel_clean_FOS**, and **UFCFlow_Sintel_final_FOS**  on google drive and open with colab notebooks Environment.
- Link Google Drive Storage with Colab Notebooks using the command:  
``` from google.colab import drive ```
``` drive.mount('/content/gdrive') ```
 - Execute each cell one by one to load the dataframes and the weights of the UFCFlow model
 - The **UFCFlow_FC_FOSwithSSIM**, **UFCFlow_FC_SOSwithSSIM** notebooks cannot be executed on the Google Colab environment since the Google Colab does not allow to extract 30GB of the Flying Chairs dataset completely. For this reason the jupter notebooks of the Flying Chairs dataset has to be executed on the local machine. 

### Making predictions
- Enter train dataframes path in variable **df**.
-  Upload the model checkpoints file on Google Drive and enter the path in variable **checkpoint_path** for each model.
-  Do not execute the two Train function cells.
-  Enter location to store flow visualizations in function ``` visualize_flow_train() ``` and ``` visualize_flow_test() ```
-  Enter test dataframes path in variable **test_df**.
-  All other instructions are commented in the notebook.

## Installation
These installation steps are for executing the UFCFlow model on the local system
- Install TensorFlow GPU - ``` pip3 install tensorflow-gpu==2.1.0```
- Install TensorFlow addons - ``` pip3 install tensorflow-addons==0.8.2```
- Install JupyterLab - ``` pip3 install jupyterlab```
- Run Jupyter Notebook - ``` jupyter notebook```
- In addition to installing the above mentioned packages, also install the required python packages such as pandas, numpy given in the notebook for successful execution of the file.
- Load the jupyter notebooks and make predictions.
- The steps for making predictions on the local system are same as above.

## References

<a id="1">[1]</a> Dosovitskiy, Alexey; Fischer, Philipp; Ilg, Eddy; Hausser, Philip; Hazirbas, Caner; Golkov, Vladimir; Van Der Smagt, Patrick; Cremers, Daniel; Brox, Thomas: Flownet: Learning optical flow with convolutional networks.

<a id="1">[2]</a> Butler, D. J.; Wulff, J.; Stanley, G. B.; Black, M. J.: A naturalistic
open source movie for optical flow evaluation.

<a id="1">[3]</a> Jason, J Y.; Harley, Adam W.; Derpanis, Konstantinos G.: Back to basics: Unsupervised learning of optical flow via brightness constancy and motion
smoothness.

<a id="1">[4]</a> Meister, Simon; Hur, Junhwa; Roth, Stefan: UnFlow: Unsupervised learning of optical flow with a bidirectional census loss.

<a id="1">[5]</a> Wang, Zhou; Bovik, Alan C.; Sheikh, Hamid R.; Simoncelli, Eero P.:
Image quality assessment: from error visibility to structural similarity.

<a id="1">[6]</a> Wang, Zhou; Bovik, Alan C.; Sheikh, Hamid R.; Simoncelli, Eero P.:
Image quality assessment: from error visibility to structural similarity.

<a id="1">[7]</a> Ren, Zhe; Yan, Junchi; Ni, Bingbing; Liu, Bin; Yang, Xiaokang; Zha,
Hongyuan: Unsupervised deep learning for optical flow estimation.