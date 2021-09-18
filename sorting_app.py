import tkinter as tk
from tkinter import ttk
from tkinter import filedialog,messagebox
import shutil,os
class Sorting_app:
    
    def __init__(self,root):
        self.root=root
        self.root.resizable(False,False)
        self.root.config(bg='white')
        self.root.title('sorting application by | Devloped by Himanshu Raj')
        self.root.geometry('1190x800+0+0')
        self.title_icon=tk.PhotoImage(file="title30.png")
        title=tk.Label(self.root,text="    Files Sorting Application",font=("impact",40),bg="#023548",fg='white',anchor=tk.W,image=self.title_icon,bd=0,relief=tk.FLAT,compound=tk.LEFT)
        title.place(x=0,y=0,relwidth=1)

                            ##>SECTION -01

        lb1_select_folder = tk.Label(self.root,text='Select Folder',font=("times new roman",25,''),bg='white')
        lb1_select_folder.place(x=50,y=120)
        self.var_folderpath=tk.StringVar()
        txt_folder_path = tk.Entry(self.root,font=('times new roman','15'),bg='lightyellow',state='readonly',textvariable=self.var_folderpath)
        txt_folder_path.place(x=300,y=120,height=40,width=600)
        browse_btn = tk.Button(self.root,text='BROWSE',font=('times new roman','15',"bold"),bg='#262626',fg ='white',activebackground='#262626',activeforeground='white',command=self.browse_function)
        browse_btn.place(x=980,y=120,height='40',width='120')
        xline = tk.Label(self.root,bg='lightgrey').place(x=50,y= 170,height=2,width=1090)
                    
                            #>> SECTION-2
        #>> All extensions
        self.image_extensions =["Image Extensions",".png",".jpg"]
        self.audio_extensions = ["Audio Extensions",".amr",".mp3"]
        self.video_extensions = ["video Extensions",".mp4",'.avi',".mpeg4",".3gp"]
        self.doc_extensions =["Document Extensions",'.doc','.xlsx','.ppt','.pptx']

        self.extensions={
                    'audios':self.audio_extensions,
                    'videos':self.video_extensions,
                    'images':self.image_extensions,
                    'documents':self.doc_extensions
                    }

        lable_2 = tk.Label(self.root,text="Various Extensions Supports",font=('times new roman','25','bold'),bg ='white')
        lable_2.place(x=50,y=190)

        self.combobox = ttk.Combobox(self.root,font=('times new roman','15'),state='readonly',justify=tk.CENTER,values=self.image_extensions)
        self.combobox.current(0)
        self.combobox.place(x=70,y=250,width=230)

        self.combobox2 = ttk.Combobox(self.root,font=('times new roman','15'),state='readonly',justify=tk.CENTER,values=self.video_extensions)
        self.combobox2.current(0)
        self.combobox2.place(x=330,y=250,width=230)

        self.combobox3 = ttk.Combobox(self.root,font=('times new roman','15'),state='readonly',justify=tk.CENTER,values=self.image_extensions)
        self.combobox3.current(0)
        self.combobox3.place(x=330+270,y=250,width=230)

        self.combobox3 = ttk.Combobox(self.root,font=('times new roman','15'),state='readonly',justify=tk.CENTER,values=self.doc_extensions)
        self.combobox3.current(0)
        self.combobox3.place(x=330+270+270,y=250,width=230)

        #>> Section Three
        #>> Image Icons 
        self.image_icon=tk.PhotoImage(file='title30.png')

        self.frame2=tk.Frame(self.root,bd=2,relief=tk.RIDGE,bg='white')
        self.frame2.place(x=50,y=310,width=1090,height=290)

        self.total_files_label = tk.Label(self.frame2,text='Total Files',font=('times new roman','18'),bg='white')
        self.total_files_label.place(x=5,y=10)

        self.total_files_image=tk.Label(self.frame2,text='',font=('times new roman','20','bold'),bg ='#0875B7',fg='white',image=self.image_icon,compound=tk.TOP,bd=4,relief=tk.RAISED)
        self.total_files_image.place(width = 200,height= 200,x=15,y=50)


        self.total_files_audios=tk.Label(self.frame2,text='',font=('times new roman','20','bold'),bg ='#0875B7',fg='white',image=self.image_icon,compound=tk.TOP,bd=4,relief=tk.RAISED)
        self.total_files_audios.place(width = 200,height= 200,x=230,y=50)
        

        self.total_files_videos=tk.Label(self.frame2,text='',font=('times new roman','20','bold'),bg ='#0875B7',fg='white',image=self.image_icon,compound=tk.TOP,bd=4,relief=tk.RAISED)
        self.total_files_videos.place(width = 200,height= 200,x=445,y=50)
        

        self.total_files_doc=tk.Label(self.frame2,text='',font=('times new roman','20','bold'),bg ='#0875B7',fg='white',image=self.image_icon,compound=tk.TOP,bd=4,relief=tk.RAISED)
        self.total_files_doc.place(width = 200,height= 200,x=660,y=50)

        self.total_files_other=tk.Label(self.frame2,text='',font=('times new roman','20','bold'),bg ='#0875B7',fg='white',image=self.image_icon,compound=tk.TOP,bd=4,relief=tk.RAISED)
        self.total_files_other.place(width = 200,height= 200,x=875,y=50)

        ##>last Section
        self.stats_label=tk.Label(self.root,text='Status',font=('times new roman',18),fg='orange',bg='white')
        self.stats_label.place(x=45,y=610)

        self.total_label=tk.Label(self.root,text='',font=('times new roman',18),fg='green',bg='white')
        self.total_label.place(x=245,y=610)

        self.moved_label=tk.Label(self.root,text='',font=('times new roman',18),fg='blue',bg='white')
        self.moved_label.place(x=445,y=610)

        self.left_label=tk.Label(self.root,text='',font=('times new roman',18),fg='red',bg='white')
        self.left_label.place(x=645,y=610)

        self.clear_btn = tk.Button(self.root,text='CLEAR',command=self.clear,font=('times new roman','15',"bold"),bg='#db2e6e',fg ='black',activebackground='#db2e6e',activeforeground='black',bd=4,relief=tk.RAISED)
        self.clear_btn.place(x=850,y=610,height='40',width='120')

        self.start_btn = tk.Button(self.root,text='START',state=tk.DISABLED,font=('times new roman','15',"bold"),bg='#03fc66',fg ='#050505',activebackground='#03fc66',activeforeground='#050505',bd=4,relief=tk.RAISED,command=self.start_fun)
        self.start_btn.place(x=980,y=610,height='40',width='120')
    
    def total_count(self):
        images=0
        audios =0
        videos =0
        documents =0
        others =0
        self.count=0
        combine_list =[]
        for i in self.all_files:
                if os.path.isfile(os.path.join(self.file_path,i)):  #>>> os.path.isfile(path) 
                   ext = '.'+i.split(".")[-1]
                   self.count+=1
                   for folder_name in self.extensions.items():
                        for x in folder_name[1]:
                           combine_list.append(x)
                        #  print(folder_name)
                        if ext.lower() in folder_name[1] and folder_name[0] == "images":
                            images+=1
                        if ext.lower() in folder_name[1] and folder_name[0] == "audios":
                            audios+=1
                        if ext.lower() in folder_name[1] and folder_name[0] == "videos":
                            videos+=1
                        if ext.lower() in folder_name[1] and folder_name[0] == "documents":
                          documents+=1

        ##>>>> this is for calculating ohters files only
        for i in self.all_files:
                if os.path.isfile(os.path.join(self.file_path,i)):
                    ext = '.'+i.split(".")[-1]
                    if ext.lower() not in combine_list:
                        others+=1  
        ##>>>>ends the functionality of other

                    self.total_files_image.config(text = 'Total Images\n'+str(images))
                    self.total_files_audios.config(text = 'Total Audios\n'+str(audios))
                    self.total_files_videos.config(text = 'Total Videos\n'+str(videos))
                    self.total_files_doc.config(text = 'Total Documents\n'+str(documents))
                    self.total_files_other.config(text = 'Other Files\n'+str(others))
                    self.total_files_label.config(text='Total Files: '+str(self.count))
    def start_fun(self):
        if self.var_folderpath.get()!='':
            self.clear_btn.config(state=tk.DISABLED)
            c=0
            for i in self.all_files:
                if os.path.isfile(os.path.join(self.file_path,i))==True:  #>>> os.path.isfile(path) 
                    c+=1 
                    self.move_func(i.split('.')[-1],i)
                    # print(f"Total Files :{length} | Done : {count} | Left:{ length-count}")
                    self.total_label.config(text='TOTAL : '+str(self.count))
                    self.moved_label.config(text='MOVED : '+str(c))
                    self.left_label.config(text='LEFT : '+str(self.count-c))


                    self.total_label.update()
                    self.moved_label.update()
                    self.left_label.update()
                    
            tk.messagebox.showinfo("Success","All files has moved successfully")
            self.start_btn.config(state=tk.DISABLED)
            self.clear_btn.config(state=tk.NORMAL)
        else:
            tk.messagebox.showerror("Error","Please Select Folder")
    def browse_function(self):
        op = tk.filedialog.askdirectory(title='SELECT FOLDER FOR SORTING')
        if len(op) > 0:  ##>>>handle folder not select error
            # print(op)
            self.var_folderpath.set(str(op))
            self.file_path = self.var_folderpath.get()
            self.all_files=os.listdir(self.file_path)
            self.otherFolder="otherfile"
            self.rename_folder()
            self.total_count()
            self.start_btn.config(state=tk.NORMAL)
            count=1
            # for i in self.all_files:
            #     if os.path.isfile(os.path.join(self.file_path,i)):  #>>> os.path.isfile(path) 
            #         move_func(i.split('.')[-1],i)
            #     print(f"Total Files :{length} | Done : {count} | Left:{ length-count}")
            #     count+=1
        else:
            pass
       
           #>>>>>>>>>>>>>>>>>>>>functionality<<<<<<<<<<<<<<<<<<
    def clear(self):
        self.start_btn.config(state=tk.DISABLED)
        self.var_folderpath.set("")
        self.total_label.config(text="")
        self.moved_label.config(text="")
        self.left_label.config(text="")

        self.total_files_image.config(text = '')
        self.total_files_audios.config(text = '')
        self.total_files_videos.config(text = '')
        self.total_files_doc.config(text = '')
        self.total_files_other.config(text = '')
        self.total_files_label.config(text='Total Files')
    def rename_folder(self):
        for folder in os.listdir(self.file_path):
            if os.path.isdir(os.path.join(self.file_path,folder)):  #>>> os.path.isfile(path) 
                os.rename(os.path.join(self.file_path,folder),os.path.join(self.file_path,folder.lower()))
    def move_func(self,ext,file_name):
        # print(f"{ext} => {file_name}")
        token =False
        for folder in self.extensions:
            if "."+ext in self.extensions[folder]:
                if folder not in os.listdir(self.file_path):
                    os.mkdir(os.path.join(self.file_path,folder))
                shutil.move(os.path.join(self.file_path,file_name),os.path.join(self.file_path,folder))
                token=True
                break
        if token != True:
            # print('run')
            if self.otherFolder not in os.listdir(self.file_path):
                os.mkdir(os.path.join(self.file_path,self.otherFolder))
            shutil.move(os.path.join(self.file_path,file_name),os.path.join(self.file_path,self.otherFolder))

root=tk.Tk()
my_object=Sorting_app(root)
root.mainloop()