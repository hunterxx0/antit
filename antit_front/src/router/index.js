import Vue from 'vue';
import VueRouter from 'vue-router';
import Signup from '../components/Signup.vue';
import Login from '../components/Login.vue';
import User from '../components/User.vue';

Vue.use(VueRouter);

const routes = [
  { path: '/signup', component: Signup },
  { path: '/login', component: Login },
  { path: '/user', component: User },
];

const router = new VueRouter({
  mode: 'history',
  routes,
});

export default router;
