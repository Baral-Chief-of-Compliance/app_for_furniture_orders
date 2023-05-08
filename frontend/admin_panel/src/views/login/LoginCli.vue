<template>

    <v-app :style="{ background: '#FF5722' }" >
        <div class="d-flex justify-center">

            <v-card width="500" height="300" class="mt-15 pa-6">
                <v-card-title>
                    Панель покупателя
                </v-card-title>
                <v-card-subtitle>
                    вход
                </v-card-subtitle>
                <v-card-item>
                    <v-text-field
                        v-model="login"
                        label="Логин"
                        color="black"
                    >
                    </v-text-field>
                    <v-text-field
                        v-model="password"
                        label="Пароль"
                        color="black"
                    >
                    </v-text-field>
                    <v-card-actions>
                        <v-btn color="red" :to="{ name: 'LoginEmployer'}">Нет, я поставщик</v-btn>
                        <v-spacer></v-spacer>
                        <v-btn color="green" @click="enter_into_system(login, password)">Войти</v-btn>
                    </v-card-actions>
                </v-card-item>
            </v-card>

        </div>

    </v-app>

</template>

<script>


</script>