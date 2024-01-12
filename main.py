import customtkinter as ctk
from pytube import YouTube

def download_video():
    url = url_entry.get()
    quality = combobox_var.get()
    
    # Show progress widgets
    progress_label.pack(pady=10)
    progress_bar.pack(pady=2, ipadx=4, ipady=2)
    status_label.pack(pady=10, ipadx=4, ipady=2)

    try:
        # Create a YouTube object
        yt = YouTube(url,on_progress_callback=on_progress_callback)
        # Filter streams based on the specified resolution
        video_stream = yt.streams.filter(res=quality).first()
        download_path = 'myvideos'
        # Download the video
        video_stream.download(download_path)

        # Update status label on successful download
        status_label.configure(text="Download successful", text_color="white", fg_color="green")

    except Exception as e:
        # Update status label on error
        status_label.configure(text=f"Error: {e}", text_color="white", fg_color="red")

def on_progress_callback(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100

    # Update progress label and bar
    progress_label.configure(text=f"{int(percentage)}%")
    progress_label.update()
    progress_bar.set(float(percentage)/100)

# Create the root window
root = ctk.CTk()

# Set window properties
root.title("Download App")
ctk.set_appearance_mode("system")  # default
ctk.set_appearance_mode("dark")
root.geometry("720x480")
root.minsize(720, 480)
root.maxsize(1080, 720)

# Create content frame
content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

# Create and pack label and entry for URL
url_label = ctk.CTkLabel(content_frame, text="Enter your URL here")
url_entry = ctk.CTkEntry(content_frame, placeholder_text="URL", width=400, height=40)
url_label.pack(padx=10, pady=10)
url_entry.pack(ipadx=4, ipady=2)
# Create a list of video qualities
qualities = ["720p", "480p", "360p"]
combobox_var = ctk.StringVar()
combobox = ctk.CTkComboBox(content_frame, values=qualities, variable=combobox_var)
combobox.set("720p")
combobox.pack(pady=10)

# Create download button
download_button = ctk.CTkButton(content_frame, text="Download", command=download_video)
download_button.pack(ipadx=5, ipady=5, pady=10)


# Create progress widgets
progress_label = ctk.CTkLabel(content_frame, text="0%")
progress_bar = ctk.CTkProgressBar(content_frame, orientation="horizontal", width=500, height=4)
progress_bar.set(0)

# Create status label
status_label = ctk.CTkLabel(content_frame, text="Downloaded", width=300)

# Run the application
root.mainloop()
