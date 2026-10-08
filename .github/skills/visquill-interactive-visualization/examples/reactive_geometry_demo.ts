/*
 * VisQuill reactive geometry demonstration ONLY.
 * Not a heat-transfer model, not a Power–Transportation dependency,
 * not compiled/browser-tested by the initial skill author.
 *
 * Build under a modern TypeScript browser scaffold after installing
 * @visquill/visquill-gdk. See official vendor API for your installed version.
 */
import { VisQuill, Reactive, Circles, Attach } from "@visquill/visquill-gdk";

/** Attach a draggable handle, a tracking circle, and a coordinate label. */
export function runDemo(host: HTMLDivElement): () => void {
  const graphic = VisQuill.create(host, "vq-demo-");
  const canvas = graphic.canvas;
  const handle = canvas.handles.disk("handle", { x: 180, y: 140 });
  const ring = canvas.visuals.circle("ring");
  const label = canvas.text.label("", "label");

  Reactive.do([handle], () => {
    Circles.circleAt(handle, 65, ring);
    label.value = `DEMO ONLY: (${Math.round(handle.x)}, ${Math.round(handle.y)})`;
  });

  Attach.pointToPoint(label, handle, { offset: { x: 0, y: -85 } });
  return () => graphic.dispose();
}
