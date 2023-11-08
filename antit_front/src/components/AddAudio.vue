<template>
    <div>
      <h2>Add Audio</h2>
      <form @submit.prevent="addAudio">
        <input type="file" ref="fileInput" />
        <input type="text" v-model="duration" placeholder="Duration in mm.ss" />
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
          this.error = 'Unable to connect to the server.';
        }
      },
    },
  };
  </script>
