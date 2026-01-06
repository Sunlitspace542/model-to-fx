## HOW TO USE
Put your 3DG1/wavefront OBJ in this folder and run "RUN.bat" (only works on Windows, Python must be installed)  
Make sure there is only one object in your .obj file, no lights, no cameras, no second mesh.  

## COLOURS FOR CONVERTING WAVEFRONT
Instead of changing the colours of materials, you now must rename the material to what colour you want to use.  
Each material name must start with "FX" then the following number for the colour you want to use.  
For example, to use the colour blue you would type FX7, an example of each colour is provided in COLOURS.txt.  
  
For colouring edges, you must create a new material and apply it to at least one face and use FE instead of FX.  
This will colour all the stray edges to the colour you choose.  

## COLOURS FOR 3DG1
Use the provided hex colours in "COLOURS.txt" that correspond to the colours in the Star Fox id_0_c palette.  

## ROUND NUMBERS
The "BLENDER round numbers.py" can be openned in Blender's scripting tab.  
Just edit the 'meshname' part to your meshes name and click the play button.  
  
However, this isn't spot on. Once you get the 3DG1 OBJ from Blender 2.4, put the file in this folder and  
select "ROUND AND COLOUR". That will round everything perfectly, though do check that it did!  

## POV-RAY EXPORT
Converts 3DG1 to a POV-RAY mesh.  
All faces MUST be tris (no quads, etc) and all faces must be white.  
Once done, OUTPUT.txt will have your model in POV-ray format.  
  
Have fun modelling!  