<template>
  <div>
    <h2>Annotate Audio</h2>
    <audio :src="audioFile" controls></audio><br/>
    <input type="text" v-model="transcription" placeholder="Enter transcription" />
    <button @click="submitTranscription">Submit</button>
    <p v-if="error" style="color: red;">{{ error }}</p>
    <h3>Old Transcriptions</h3>
    <table v-if="oldTranscriptions && oldTranscriptions.length > 0">
      <thead>
        <tr>
          <th>Transcription Text</th>
          <th>User Name</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="transcript in oldTranscriptions" :key="transcript.id">
          <td>{{ transcript.transcription }}</td>
          <td>{{ transcript.user_name }}</td>
        </tr>
      </tbody>
    </table>
    <p v-else>No old transcriptions available.</p>
  </div>
</template>

<script>
export default {
  name: 'AnnotateAudio',
  data() {
    return {
      audioId: null,
      audioFile: '',
      transcription: '',
      error: null,
      oldTranscriptions: [],
    };
  },
  computed: {
    transcriptionExists() {
      const currentUserID = localStorage.getItem('user');
      return this.oldTranscriptions.some(
        transcript => transcript.user === Number(currentUserID)
      );
    },
  },
    methods: {
      async submitTranscription() {
        const user = localStorage.getItem('user')
        const token = localStorage.getItem('token');
        let method, audioId, url = null

        if (this.transcriptionExists) {
          const userTranscription = this.oldTranscriptions.find(
            transcript => transcript.user === Number(user)
          );
          audioId = userTranscription.audio
          url = `http://localhost:8000/api/transcription/${this.audioId}/transcription/update/${userTranscription.id}/`
          method = 'PUT'
        } else {
          audioId = this.audioId
          url = `http://localhost:8000/api/transcription/${this.audioId}/transcriptions/`
          method = 'POST'

        }
        const response = await fetch(
          url,
          {
            method: method,
            headers: {
              'Content-Type': 'application/json',
              Authorization: `Token ${token}`,
            },
            body: JSON.stringify({
              audio: audioId,
              user: user,
              transcription: this.transcription,
            }),
          }
        );
        if (response.ok) {
          await this.fetchOldTranscriptions();
          this.transcription = '';
          this.error = null;
        } else {
          const data = await response.json();
          this.error = data.failed;
        }
      },

    async fetchAudio() {
      try {
        const audioId = this.$route.params.audioId;
        const token = localStorage.getItem('token');
        const response = await fetch(`http://localhost:8000/api/audio/audio/${audioId}`, {
          headers: {
            Authorization: `Token ${token}`,
          },
        });
        if (response.ok) {
          const data = await response.json();
          this.audioFile = data.audio_file;
        } else {
          throw new Error('Unable to fetch audio.');
        }
      } catch (error) {
        console.error(error);
        alert('Unable to connect to the server.');
      }
    },
    async fetchOldTranscriptions() {
      try {
        const audioId = this.$route.params.audioId;
        const response = await fetch(`http://localhost:8000/api/transcription/${audioId}/transcriptions/`);
        if (response.ok) {
          const data = await response.json();
          this.oldTranscriptions = data;
                  } else {
          throw new Error('Unable to fetch old transcriptions.');
        }
      } catch (error) {
        console.error(error);
        alert('Unable to connect to the server.');
      }
    },
  },
  mounted() {
    this.audioId = this.$route.params.audioId;
    this.fetchAudio();
    this.fetchOldTranscriptions();
  },
};
</script>