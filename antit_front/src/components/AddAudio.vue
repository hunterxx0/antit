<template>
    <div>
      <h2>Add Audio</h2>
      <form @submit.prevent="addAudio">
        <input type="file" ref="fileInput" @change="getFileDuration" accept="audio/*" />
        <p v-if="duration">Duration: {{ duration }} seconds</p>
        <button type="submit">Add</button>
      </form>
      <p v-if="error" style="color: red;">{{ error }}</p>
    </div>
  </template>

  <script>
  export default {
    name: 'AddAudio',
    data() {
      return {
        duration: null,
        error: null,
      };
    },
    methods: {
      async addAudio() {
        try {
          if (!this.duration) {
            throw new Error('Please select an audio file.');
          }

          const token = localStorage.getItem('token');
          const formData = new FormData();
          formData.append('audio_file', this.$refs.fileInput.files[0]);
          formData.append('duration', this.duration);
          const response = await fetch('http://localhost:8000/api/audio/audio/', {
            method: 'POST',
            headers: {
              Authorization: `Token ${token}`,
            },
            body: formData,
          });
          if (response.ok) {
            alert('Audio added successfully!');
            this.$router.push('/hello-user');
          } else {
            throw new Error('Unable to add audio.');
          }
        } catch (error) {
          console.error(error);
          this.error = error.message;
        }
      },
      getFileDuration(event) {
        const file = event.target.files[0];

        if (file.type.startsWith('audio/')) {
          const audio = document.createElement('audio');
          audio.src = URL.createObjectURL(file);
          audio.onloadedmetadata = () => {
            this.duration = audio.duration.toFixed(2);
            URL.revokeObjectURL(audio.src);
          };
        } else {
          this.duration = null;
          this.error = 'Unsupported file type. Please select an audio file.';
        }
      },
    },
  };
  </script>
