<template>
  <MainPage>
    <div class="container mt-5">
      <div class="row justify-content-center">
        <div class="col-md-6">
          <div class="card">
            <div class="card-body">
              <h2 class="card-title text-center mb-4">Add Audio</h2>
              <form @submit.prevent="addAudio">
                <div class="mb-3">
                  <label for="fileInput" class="form-label">Choose Audio File</label>
                  <input type="file" ref="fileInput" @change="getFileDuration" class="form-control" accept="audio/*" />
                </div>
                <p v-if="duration" class="mb-3">Duration: {{ duration }} seconds</p>
                <button class="btn btn-primary w-100" type="submit">Add</button>
              </form>
              <p v-if="error" class="mt-3 text-danger text-center">{{ error }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </MainPage>
</template>

<script>
import MainPage from '@/components/MainPage.vue';

export default {
  components: {
    MainPage,
  },
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
        const response = await fetch('http://bed507c2346c.c2b96c85.hbtn-cod.io:8000/api/audio/audio/', {
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

<style scoped>
.card {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
</style>
