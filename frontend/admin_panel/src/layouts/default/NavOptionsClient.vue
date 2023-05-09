<template>
    <v-list-group value="Students">
    <template v-slot:activator="{ props }">
      <v-list-item
        v-bind="props"
        prepend-icon="mdi-table-large"
        title="Категории"
      ></v-list-item>
    </template>

    <v-list-item
      v-for="([title, icon, to], i) in categories"
      :key="i"
      :title="title"
      :prepend-icon="icon"
      :value="title"
      :to="to"
    ></v-list-item>
  </v-list-group>

  <v-list-group value="Orders">
    <template v-slot:activator="{ props }">
      <v-list-item
        v-bind="props"
        prepend-icon="mdi-package-variant-closed"
        title="Заказы"
      ></v-list-item>
    </template>

    <v-list-item
      v-for="([title, icon, to], i) in orders"
      :key="i"
      :title="title"
      :prepend-icon="icon"
      :value="title"
      :to="to"
    ></v-list-item>

    
  </v-list-group>

</template>

<script>
  export default {
    data: () => ({
      categories: [
        ['Добавить', 'mdi-table-plus', '/operator/categories']
      ],
      orders:[
        ['Список', 'mdi-animation', '/teachers'],
        ['Добавить', 'mdi-package-variant', '/teachers']
      ],
    }),
  }
</script>