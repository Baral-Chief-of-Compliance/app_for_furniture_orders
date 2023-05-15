// Composables
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    component: () => import('@/layouts/default/Default.vue'),
    children: [
      {
        path: '',
        name: 'Home',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "home" */ '@/views/Home.vue'),
      },
      {
        path: 'operator/categories',
        name: 'add_category',
        component: () => import('@/components/categories/Categories.vue')
      },
      {
        path: 'operator/categories/:id',
        name: 'category',
        component: () => import('@/components/categories/Categorie.vue')
      }
    ],
  },
  {
    path: '/login-employer',
    name: 'LoginEmployer',
    component: () => import('@/views/login/LoginEmp.vue')
  },
  {
    path: '/login-client',
    name: 'LoginClient',
    component: () => import('@/views/login/LoginCli.vue')
  },
  {
    path: '/client',
    component: () => import('@/layouts/default/DefaultClient.vue'),
    children: [
      {
        path: '',
        name: 'Home',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "home" */ '@/views/Home.vue'),
      },
      {
        path: 'providers',
        name: 'ClientProviders',
        component: () => import('@/components/client/ClientsProviders.vue')
      },
      {
        path: 'providers/:id_p',
        name: 'ClientProvider',
        component: () => import('@/components/client/ClientsProvider.vue')
      },
      {
        path: 'providers/:id_p/category/:cat_id',
        name: 'ProviderCategory',
        component: () => import('@/components/client/ProviderCategory.vue')
      },
      {
        path: 'providers/:id_p/category/:cat_id/product/:id_product',
        name: 'ProviderProduct',
        component: () => import('@/components/client/ProviderProduct.vue')
      },
      {
        path: 'basket',
        name: 'ClientBasket',
        component: () => import('@/components/client/ClientBasket.vue')
      },
      {
        path: 'create_application',
        name: 'ClientCreateApplication',
        component: () => import('@/components/client/ClientCreateApplication.vue')
      },
      {
        path: 'active_client_applications',
        name: 'ActiveClientApplications',
        component: () => import('@/components/client/ActiveClientApplications.vue')
      },
      {
        path: 'close_client_applications',
        name: 'CloseClientApplications',
        component: () => import('@/components/client/CloseClientApplications.vue')
      },
      {
        path: 'client_application_inf',
        name: 'ClientApplicationInf',
        component: () => import('@/components/client/ClientApplicationInf.vue')
      },
      {
        path: 'client_products',
        name: 'ClientProducts',
        component: () => import('@/components/client/ClientProducts.vue')
      }
    ],
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
