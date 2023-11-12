<template>
  <MainPage>
    <div class="container-fluid text-center">
      <h2>Hello, {{ user }}!</h2>

      <div v-if="allAudiosAnnotated">
        <h4 class="text-success">All the audios are annotated!</h4>
      </div>

      <div v-else-if="audios && audios.length > 0" class="table-responsive">
        <table class="table table-striped table-bordered">
          <thead>
            <tr>
              <th>Filename</th>
              <th>Duration</th>
              <th>Number of Transcriptions</th>
              <th>Annotated</th>
              <th v-if="!allAudiosAnnotated">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="audio in audios" :key="audio.id">
              <td>{{ audio.filename }}</td>
              <td>{{ audio.duration }}</td>
              <td>{{ audio.transcription_count }}</td>
              <td>
                <i v-if="audio.annotated" class="text-success bi bi-check" style="font-size: 1.5em;"></i>
                <i v-else class="text-danger bi bi-x" style="font-size: 1.5em;"></i>
              </td>
              <td v-if="!allAudiosAnnotated">
                <button
                  class="btn btn-primary"
                  @click="annotateAudio(audio)"
                >
                  {{ audio.annotated ? 'Edit' : 'Annotate' }}
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <p v-else>Loading...</p>
    </div>
  </MainPage>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.min.css';
import MainPage from '@/components/MainPage.vue';

export default {
  components: {
    MainPage,
  },
  name: 'HelloUser',
  data() {
    return {
      user: '',
      user_id:'',
      audios: null,
    };
  },
  computed: {
    allAudiosAnnotated() {
      return this.audios && this.audios.every(audio => audio.annotated);
    },
  },
  methods: {
    getUsernameFromToken() {
      const token = localStorage.getItem('access');
      try {
        if (token) {
          const decodedToken = this.parseJwt(token);
          let username = decodedToken.username;
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
        const user_id = localStorage.getItem('user')
        const response = await fetch(`http://bed507c2346c.c2b96c85.hbtn-cod.io:8000/api/audio/audio/?user_id=${user_id}`, {
          headers: {
            Authorization: `Token ${token}`,
          },
        });
        if (response.ok) {
          const data = await response.json();
          for (const audio of data) {
            const path = audio.audio_file;
            const nameIndex = path.lastIndexOf('/');
            const name = path.slice(nameIndex + 1);
            audio.filename = name;
          }
          this.audios = data;
        } else {
          throw new Error('Unable to fetch audios.');
        }
      } catch (error) {
        console.error(error);
        alert('Unable to connect to the server.');
        this.$router.push('/login');
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
