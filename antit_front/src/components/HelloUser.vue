<template>
  <div>
    <h2>Hello, {{ user.username }}!</h2>
    <button @click="fetchAudios">Refresh</button>
    <ul v-if="audios">
      <li v-for="audio in audios" :key="audio.id">
        <p>Filename: {{ audio.filename }}</p>
        <p>Duration: {{ audio.duration }}</p>
        <p>Number of transcriptions: {{ transcriptionCount }}</p>
        <button @click="annotateAudio(audio)">Annotate</button>
      </li>
    </ul>
    <p v-else>Loading...</p>
    <router-link to="/add-audio">Add Audio</router-link>
  </div>
</template>

<script>
export default {
  name: 'HelloUser',
  data() {
    return {
      user: '',
      audios: null,
      transcriptionCount: null,
    };
  },
  methods: {
    getUsernameFromToken() {
      const token = localStorage.getItem('access');
      try {
        if (token) {
          const decodedToken = this.parseJwt(token);
          let username = decodedToken.username
          username = username.charAt(0).toUpperCase() + username.slice(1);
          this.user = username;
        } else {
          console.error('Token is missing');
          this.$router.push('/login');
        }
      } catch (error) {
        console.error('Invalid token:', error);
        this.$router.push('/login');
      }
    },
    parseJwt(token) {
      try {
        return JSON.parse(atob(token.split('.')[1]));
      } catch (e) {
        return {};
      }
    },
    async fetchAudios() {
      try {
        const token = localStorage.getItem('token');
        const response = await fetch('http://localhost:8000/api/audio/audio/', {
          headers: {
            Authorization: `Token ${token}`,
          },
        });
        if (response.ok) {
          const data = await response.json();
          for (const audio of data) {
            await this.fetchTranscriptionCount(audio);
          }
          this.audios = data;
        } else {
          throw new Error('Unable to fetch audios.');
        }
      } catch (error) {
        console.error(error);
        alert('Unable to connect to the server.');
      }
    },
    async fetchTranscriptionCount(audio) {
      try {
        const response = await fetch(`http://localhost:8000/api/transcription/${audio.id}/transcription_number/`);
        if (response.ok) {
          const data = await response.json();
          audio.transcriptionCount = data.count;
        } else {
          audio.transcriptionCount = 0;
        }
      } catch (error) {
        console.error(error);
        alert('Unable to connect to the server.');
      }
    },
    annotateAudio(audio) {
      this.$router.push({ name: 'AnnotateAudio', params: { audioId: audio.id } });
    },
  },
  async mounted() {
    this.getUsernameFromToken();
    await this.fetchAudios();
  },
};
</script>
