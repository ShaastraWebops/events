function varargout = try2(varargin)
% TRY2 MATLAB code for try2.fig
%      TRY2, by itself, creates a new TRY2 or raises the existing
%      singleton*.
%
%      H = TRY2 returns the handle to a new TRY2 or the handle to
%      the existing singleton*.
%
%      TRY2('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in TRY2.M with the given input arguments.
%
%      TRY2('Property','Value',...) creates a new TRY2 or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before try2_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to try2_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help try2

% Last Modified by GUIDE v2.5 29-Nov-2013 18:32:08

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @try2_OpeningFcn, ...
                   'gui_OutputFcn',  @try2_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT
end


% --- Executes just before try2 is made visible.
function try2_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to try2 (see VARARGIN)


handles.ser=instrfind;    
si=size(handles.ser);   
fclose(handles.ser(si(2)));           

handles.ser=serial('COM20','BAUD',115200);
fopen(handles.ser);
disp('done');

pause(1);

while(~handles.ser.BytesAvailable)            
    disp('loop')
end

disp('Yes')
    
handles.first=[1:1:10];
handles.second=[1:0.5:10];
handles.third=[1:0.25:10];
handles.current=handles.first;

handles.mul=1;
plot(sin(handles.mul*handles.current));

% Choose default command line output for try2
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);
end
    

% UIWAIT makes try2 wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = try2_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;
end


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
plot(sin(handles.mul*handles.current));
end


% --- Executes on selection change in popupmenu1.
function popupmenu1_Callback(hObject, eventdata, handles)
% hObject    handle to popupmenu1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = cellstr(get(hObject,'String')) returns popupmenu1 contents as cell array
%        contents{get(hObject,'Value')} returns selected item from popupmenu1

var=get(hObject,'Value');

switch var
    case 1
        handles.current=handles.first;
    case 2
        handles.current=handles.second;
    case 3
        handles.current=handles.third;                        
end

guidata(hObject,handles)                   
end  


% --- Executes during object creation, after setting all properties.
function popupmenu1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to popupmenu1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
end

% --- Executes on button press in togglebutton1.
function togglebutton1_Callback(hObject, eventdata, handles)
% hObject    handle to togglebutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of togglebutton1

% if (get(handles.togglebutton1,'Value'))           
%     set(handles.text1,'String','hello')
% else
%     set(handles.text1,'String','bye')
% end
% guidata(hObject,handles);                

flag=1;
while(get(hObject,'Value'))           
    if(flag)
        build    
    end
    flag=0;
    if(handles.ser.BytesAvailable)
        a=str2num(fscanf(handles.ser));        
        place(a,50,0);
    end        
    pause(0.4);
end
set(handles.text1,'String','nothing');
guidata(hObject,handles);

% while(get(hObject,'Value'))
%     disp('llopw');
%     pause(0.1);
% end


end 

function place(x,y,t,~)
                
    figure(1);
    r1=380;
    r2=380;
    r3=380;
    r4=380;
    
    r5=500;          
    
    bcol=[1,1,1];
    l1=line([x,x+r1*cos(t)],[y,y+r1*sin(t)],'color',[0.6,0.6,0.6]);
    l2=line([x,x-r2*sin(t)],[y,y+r2*cos(t)],'color',bcol);
    l3=line([x,x-r3*cos(t)],[y,y-r3*sin(t)],'color',bcol);
    l4=line([x,x+r4*sin(t)],[y,y-r4*cos(t)],'color',bcol);
    l5=line([x,x+r5*cos(t+pi/4)],[y,y+r5*sin(t+pi/4)],'color',bcol);

    plot(x,y,'color',bcol);
    
    drawnow
    
    pause(0.040)
    if(nargin==3)
        delete(l1,l2,l3,l4,l5);
    end
    
    drawnow
end