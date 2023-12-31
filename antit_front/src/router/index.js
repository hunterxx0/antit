import { createRouter, createWebHistory } from 'vue-router';
import Login from '@/components/LoginView.vue';
import SignUp from '@/components/SignUp.vue';
import HelloUser from '@/components/HelloUser.vue';
import AnnotateAudio from '@/components/AnnotateAudio.vue';
import AddAudio from '@/components/AddAudio.vue';

const routes = [
  { path: '/login', component: Login },
  { path: '/signup', component: SignUp },
  { path: '/hello-user', component: HelloUser },
  { path: '/', redirect: '/login' },
  { path: '/annotate/:audioId', name: 'AnnotateAudio', component: AnnotateAudio },
  { path: '/add-audio', component: AddAudio },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
