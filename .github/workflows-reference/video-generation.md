# Video Generation from Images Workflow

This document explains how to convert a sequence of image files (e.g., screenshots or figure panels) into an `.mp4` video that loops automatically in Quarto. This is particularly useful for showing time-courses or smooth transitions (crossfades) between data maps.

## 1. Simple Slideshow (No Crossfades)

When the user has a sequence of multiple images (e.g., `Screenshot 1.png`, `Screenshot 2.png`, etc.) and wants them to advance slowly (e.g., one image every 2 seconds) like a flipbook, use the following `ffmpeg` command:

```bash
ffmpeg -f image2 -pattern_type glob -framerate 0.5 -i '*.png' -c:v libx264 -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" -y output.mp4
```

**Key Parameters:**
* `-framerate 0.5`: Display each frame for 2 seconds (1 / 0.5). For 1 FPS, use `-framerate 1`.
* `-pattern_type glob -i '*.png'`: Collect all matching PNGs in alphabetical/lexicographical order.
* `scale=trunc(iw/2)*2:trunc(ih/2)*2`: Ensures video dimensions are divisible by 2, which is strictly required for the `yuv420p` pixel format.
* `-c:v libx264 -pix_fmt yuv420p`: Uses the H.264 codec and a pixel format that ensures maximum compatibility across all standard web browsers.

## 2. Smooth Looping Crossfade (Blend between two images)

When the user has two or more images and wants a smooth transition (crossfade) that loops perfectly, the process requires more explicit `ffmpeg` filters. 

*Note: For the `xfade` filter to parse correctly without escaping issues, it is highly recommended to rename the images to simple names (e.g., `1.png` and `2.png`) prior to running the command.*

```bash
# Example preprocessing to simplify filenames
mv "complex name A.png" 1.png
mv "complex name B.png" 2.png

# Generate the crossfaded video
ffmpeg -loop 1 -t 3 -i 1.png \
       -loop 1 -t 4 -i 2.png \
       -loop 1 -t 1 -i 1.png \
       -filter_complex "\
       [0:v]scale=trunc(iw/2)*2:trunc(ih/2)*2,framerate=fps=30[v0]; \
       [1:v]scale=trunc(iw/2)*2:trunc(ih/2)*2,framerate=fps=30[v1]; \
       [2:v]scale=trunc(iw/2)*2:trunc(ih/2)*2,framerate=fps=30[v2]; \
       [v0][v1]xfade=transition=fade:duration=1:offset=2[f1]; \
       [f1][v2]xfade=transition=fade:duration=1:offset=5[out]" \
       -map "[out]" -c:v libx264 -pix_fmt yuv420p -y output.mp4
```

**How the math works for the perfect loop:**
* `Input 0` provides Image 1 for an initial base duration (3 seconds).
* `Input 1` provides Image 2 for a secondary duration (4 seconds).
* `Input 2` provides Image 1 for a tail duration (1 second). This matches the end of the video exactly to the start of the video.
* `offset=2` begins the `duration=1` crossfade from Image 1 to Image 2 at the 2-second mark.
* `offset=5` begins the `duration=1` crossfade from Image 2 back to Image 1 at the 5-second mark.
* **The Result:** The video is exactly 6 seconds long. The first frame (0s) and the final frame (6s) are exactly Image 1. When the Quarto HTML plays the video in a `loop`, the transition back to the start occurs invisibly.

## 3. Quarto Insertion

After creating the `.mp4` video, embed it in a `.qmd` file with the standard Quarto-style image syntax mapping. Append the attributes to force the video to behave like a GIF (invisibly re-looping and automatically autoplaying).

```markdown
![Video Caption Here](path/to/output.mp4){#vid-unique-label width="80%" loop="true" autoplay="true" muted="true"}
```

**Important:** Nearly all modern browsers enforce strict autoplay policies. A video will only respect `autoplay="true"` if `muted="true"` is also explicitly defined.