<template>
    <div class=" w-fit absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2
        grid gap-4
        md: grid-cols-4
        lg: grid-cols-6
        xl: grid-cols-8">
        <main-card v-for="item in items" :key="item.id"></main-card>
    </div>
</template>

<script>
import { defineComponent, ref } from 'vue';
import MainCard from '@/components/MainCard.vue';

export default defineComponent({
    name: 'MainView',
    components: {
        'main-card': MainCard
    },
    setup() {
        const items = Array.from({ length: 48 }, (_, index) => ({
            id: index, // 或者任何其他你想要为每个 div 设置的唯一标识符
            // 其他你需要的数据属性
        }));
        const cardRefs = ref([]);

        return {items, cardRefs};
    }
})

</script>