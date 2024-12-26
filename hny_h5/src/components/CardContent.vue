<template>
    <div class="flex flex-col w-80 h-fit bg-cyan-500 items-center gap-4">
        <div class="w-full h-12 bg-fuchsia-500"></div>
        <div class="w-full h-fit bg-fuchsia-600 flex flex-col p-4 gap-4">
            <div class="w-full h-12 bg-white"></div>
            <div class="w-full h-fit bg-white flex gap-4">
                <div class="w-6 h-40 bg-slate-500"></div>
                <div class="w-6 h-40 bg-slate-500"></div>
                <div class="w-6 h-40 bg-slate-500"></div>
                <div class="w-6 h-40 bg-slate-500"></div>
                <div class="w-6 h-40 bg-slate-500"></div>
                <div class="w-auto flex-grow h-40 bg-orange-500"></div>
            </div>
            <div class="w-full h-1 bg-white"></div>
            <div class="w-full h-auto flex-grow bg-white flex flex-col gap-4">
                <div class="w-20 h-6 bg-slate-500"></div>
                <div class="w-full h-16 bg-slate-500"></div>
                <div class="w-20 h-6 bg-slate-500"></div>
                <div class="w-full h-16 bg-slate-500"></div>
            </div>
        </div>
        <div class="flex w-full h-fit justify-between gap-4">
            <div class="w-full h-12 bg-white"></div>
            <div class="w-full h-12 bg-red-500" @click.stop="test_close"></div>
        </div>
    </div>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'CardContent',
    methods: {
        test_close() {
            this.$emit(
                'getCloseStatu',
                {
                    'close': true
                }
            )
        }
    }
})
</script>