clear
clc
%User Defined Properties 
a = arduino('COM5','uno');            % define the Arduino Communication port
plotTitle = 'Arduino Data Log - Bicep Readings';  % plot title
xLabel = 'Elapsed Time (s)';     % x-axis label
yLabel = 'Surface EMG';      % y-axis label
legend1 = 'Measured Voltage Scaled by 100';
yMax  = 500;                          %y Maximum Value
yMin  = -200;                     %y minimum Value
plotGrid = 'on';                 % 'off' to turn off grid
min = -200;                         % set y-min
max = 500;                        % set y-max
delay = .05;                     % make sure sample faster than resolution 
%Define Function Variables
time = 0;
data = 0;
data1 = 0;
data2 = 0;
count = 0;
%Calculating parameters for 60Hz Notch Filter
F0 = 60;   % Interference is at 60 Hz
Fs = 1/0.005; % previously 1/0.005
BW = 6;    % Choose a bandwidth factor of 6Hz
[num1,den1] = iirnotch(F0/(Fs/2),BW/(Fs/2));

%Visualizing frequency spectrum for notch filter
%fvtool(num1,den1,'Fs',Fs,'Color','white');


%Set up Plot
plotGraph = plot(time, data, '-r' );  % every readVoltage needs to be on its own Plotgraph
hold on                            %hold on makes sure all of the channels are plotted
title(plotTitle,'FontSize',15);
xlabel(xLabel,'FontSize',15);
ylabel(yLabel,'FontSize',15);
legend(legend1)
axis([yMin yMax min max]);
grid(plotGrid);
tic

while ishandle(plotGraph) %Loop when Plot is Active will run until plot is closed
        dat = readVoltage(a,'A5') ;   %Data from the arduino
        if (dat > 30)
            %playTone(a,'D10',500,1);
        end
        dat = filter(num1, den1, dat);
        dat = dat*500;
        count = count + 1;    
        time(count) = toc;    
        data(count) = dat(1);   
        set(plotGraph,'XData',time,'YData',data);    %%using regular 'plot' slows down the sampling rate inconsistently
        axis([0 time(count) min max]);
        %Update the graph
        pause(delay);             %10kHz sampling frequency
 end
clear a
disp('Plot Closed and arduino object has been deleted')