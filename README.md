# FYP-SuperResolution
Final Year Project. Image Super-Resolution<br>
## Here's how to  crappify data:

  1) Clone Repo

  2) Create a folder Hierarchy as such :
  ```
      root
      |__DataSet
         |__Hi-Res
         |  <save high resolution files here>
         |__Low-Res
            |__OneHalf
            |__OneFourth
            |__OneEighth
            |__OneSixteenth
  ```
  3) Copy your high-resolution images into `DataSet/Hi-Res`
  4) Open your command prompt in the root of the repo
  5) run `python Crappify.py -l "DataSet"`
