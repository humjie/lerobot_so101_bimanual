import cv2
import time
import sys

def test_camera(device_index=0):
    print(f"--- Attempting to open camera at index {device_index} ---")
    cap = cv2.VideoCapture(device_index)

    if not cap.isOpened():
        print(f"Error: Could not open video device {device_index}.")
        print("Tip: Run 'v4l2-ctl --list-devices' to find the correct index.")
        return

    # --- KEY CONFIGURATION BASED ON YOUR SPECS ---
    # The spec sheet says 1920x1080 is MJPG. 
    # We force MJPG here to prevent USB bandwidth errors.
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    cap.set(cv2.CAP_PROP_FOURCC, fourcc)

    # Resolution Settings (Try 1920x1080 first, or switch to 640x480)
    # width, height = 1920, 1080  # Max resolution from spec sheet
    width, height = 640, 480    # Standard resolution from spec sheet
    
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    cap.set(cv2.CAP_PROP_FPS, 30)

    # Read the actual values set by the camera to verify
    actual_w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    actual_h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    actual_fps = cap.get(cv2.CAP_PROP_FPS)
    codec = int(cap.get(cv2.CAP_PROP_FOURCC))
    codec_str = "".join([chr((codec >> 8 * i) & 0xFF) for i in range(4)])

    print(f"\nCamera Initialized:")
    print(f"  - Resolution: {int(actual_w)}x{int(actual_h)}")
    print(f"  - FPS Setting: {actual_fps}")
    print(f"  - Codec: {codec_str} (Should be MJPG for high res)")
    print("\nPress 'q' to quit.")

    prev_time = time.time()
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to grab frame.")
            break

        # Calculate actual FPS for display
        current_time = time.time()
        frame_count += 1
        elapsed = current_time - prev_time
        
        if elapsed >= 1.0:
            print(f"Status: capturing at {frame_count / elapsed:.1f} FPS")
            prev_time = current_time
            frame_count = 0

        # Show the feed
        cv2.imshow(f'Camera Test (Index {device_index})', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # You can pass the camera index as an argument (default is 0)
    # Example: python test_camera.py 4
    idx = 0
    if len(sys.argv) > 1:
        try:
            idx = int(sys.argv[1])
        except ValueError:
            print("Invalid index provided. Using 0.")
    
    test_camera(idx)