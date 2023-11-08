<template>
    <div>
      <h2>Annotate Audio</h2>
      <audio :src="audioFile" controls></audio>
      <input type="text" v-model="transcription" placeholder="Enter transcription" />
      <button @click="submitTranscription">Submit</button>
      <p v-if="error" style="color: red;">{{ error }}</p>
      <h3>Old Transcriptions</h3>
      <ul>
        <li v-for="transcript in oldTranscriptions" :key="transcript.id">
          <p>Text: {{ transcript.transcription }}</p>
          <p>User: {{ transcript.user.name }}</p>
        </li>
      </ul>
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
        try {
          const response = await fetch(`http://localhost:8000/api/transcription/${this.audioId}/transcribe/transcription/`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              audio: this.audioId,
              user: JSON.parse(localStorage.getItem('user')).id,
            transcription: this.transcription,
          }),
        });
        if (response.ok) {
            await this.fetchOldTranscriptions();
            this.$refs.textInput.disabled = true;
            this.$refs.submitButton.disabled = true;
        } else {
          const data = await response.json();
          throw new Error(data.detail);
        }
      } catch (error) {
        console.error(error);
        this.error = error.message;
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
        const response = await fetch(`http://localhost:8000/api/transcription/${audioId}/transcription/`);
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