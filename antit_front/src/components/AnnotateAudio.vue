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
    methods: {
      async submitTranscription() {
        const user = localStorage.getItem('user')
        const token = localStorage.getItem('token');
        console.log(user)
        if (user) {
            const response = await fetch(`http://localhost:8000/api/transcription/${this.audioId}/transcribe/transcription/`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Token ${token}`,
            },
            body: JSON.stringify({
              audio: this.audioId,
              user: user,
              transcription: this.transcription,
            }),
        });
        if (response.ok) {
            await this.fetchOldTranscriptions();
            this.$refs.textInput.disabled = true;
            this.$refs.submitButton.disabled = true;
        } else {
          const data = await response.json();
          console.log(response)
          console.log(data)
        //   throw new Error(data.detail);
        }
        }else {
            this.$router.push('/login');
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
        const response = await fetch(`http://localhost:8000/api/transcription/${audioId}/transcribe/transcription/`);
        if (response.ok) {
          const data = await response.json();
          console.log(data)
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