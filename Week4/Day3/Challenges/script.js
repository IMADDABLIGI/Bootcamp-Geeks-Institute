class Video{
    constructor(title, uploader, time){
        this.title = title;
        this.uploader = uploader;
        this.time = time; // time in seconds
    }

    watch(){
        console.log(`uploader ${this.uploader} watched all time ${this.time} of title ${this.title}!`)
    }

}

let mp4 = new Video("mp4", "uploader1", 120);
mp4.watch();

let openheimer = new Video("Oppenheimer", "uploader2", 180);
openheimer.watch();
