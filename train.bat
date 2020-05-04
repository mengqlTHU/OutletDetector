opencv_createsamples -vec outlet.vec -info pos.lst -num 401 -w 24 -h 24
opencv_traincascade -data classifier -vec outlet.vec -bg neg.lst -numPos 380 -numNeg 300 -numStages 15 -w 24 -h 24