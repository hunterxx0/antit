<template>
  <div>
    <h2>Hello, {{ username }}!</h2>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
    };
  },
  mounted() {
    this.getUsernameFromToken();
  },
  methods: {
    getUsernameFromToken() {
      const token = localStorage.getItem('access');
      console.log('Token:', token);
      try {
        if (token) {
          const decodedToken = this.parseJwt(token);
          console.log('Decoded Token:', decodedToken);
          this.username = decodedToken.username;
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
  },
};
</script>
