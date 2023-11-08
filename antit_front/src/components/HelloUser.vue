<template>
  <div>
    <h2>Hello, {{ user }}!</h2>
    <router-link to="/add-audio">Add Audio</router-link> <br>
    <button @click="fetchAudios">Refresh</button>
    <table v-if="audios">
      <thead>
        <tr>
          <th>Filename</th>
          <th>Duration</th>
          <th>Number of Transcriptions</th>
          <th>Annotate</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="audio in audios" :key="audio.id">
          <td>{{ audio.filename }}</td>
          <td>{{ audio.duration }}</td>
          <td>{{ audio.transcription_count }}</td>
          <td><button @click="annotateAudio(audio)">Annotate</button></td>
        </tr>
      </tbody>
    </table>
    <p v-else>Loading...</p>
  </div>
</template>

<script>
export default {
  name: 'HelloUser',
  data() {
    return {
      user: '',
      audios: null,
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
          localStorage.setItem('user', decodedToken.user_id);
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
            const path = audio.audio_file
            const nameIndex = path.lastIndexOf("/");
            const name = path.slice(nameIndex+1);
            audio.filename = name
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
